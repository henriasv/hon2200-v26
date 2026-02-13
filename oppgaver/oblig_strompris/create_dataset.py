"""
Datakureringsscript for obligatorisk oppgave om strømprisklassifisering.

Henter data fra tre kilder:
  1. hvakosterstrommen.no — daglige spotpriser for NO1 (gratis, ingen nøkkel)
  2. Frost API (met.no) — værdata fra stasjon SN18700 (Blindern)
  3. NVE — ukentlig magasinfylling for NO1-området

Kjøres én gang for å generere datasettet.

Avhengigheter:
    pip install requests pandas numpy

Du trenger en Frost API-nøkkel (gratis): https://frost.met.no/howto.html
Sett miljøvariabelen FROST_CLIENT_ID, eller endre konstanten i scriptet.

OBS: Dette scriptet er LLM-generert basert på instruksjoner fra faglærer.
"""

import pandas as pd
import numpy as np
import requests
import datetime
import time
import os
import sys
import json
import urllib.request

# ============================================================
# KONFIGURASJON — Sett FROST_CLIENT_ID som miljøvariabel
# eller endre default-verdien her
# ============================================================
FROST_CLIENT_ID = os.environ.get(
    "FROST_CLIENT_ID", "SETT_INN_DIN_FROST_CLIENT_ID"
)

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "strompris_oslo.csv")

START_DATE = datetime.date(2022, 1, 1)
END_DATE = datetime.date(2024, 12, 31)

SEED = 42
# ============================================================


def hent_strompriser(start, slutt):
    """Henter daglige snittpriser fra hvakosterstrommen.no (NO1).

    API-et returnerer 24 timeverdier per dag i NOK/kWh.
    Vi beregner daglig snitt og konverterer til øre/kWh.
    """
    records = []
    current = start
    total_days = (slutt - start).days + 1
    errors = 0

    while current <= slutt:
        day_num = (current - start).days + 1
        if day_num % 100 == 0 or day_num == 1:
            print(f"  Dag {day_num}/{total_days}: {current}")

        url = (
            f"https://www.hvakosterstrommen.no/api/v1/prices/"
            f"{current.year}/{current.month:02d}-{current.day:02d}_NO1.json"
        )
        try:
            req = urllib.request.Request(url)
            req.add_header("User-Agent", "HON2200-dataset-script/1.0")
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read())

            prices_nok = [h["NOK_per_kWh"] for h in data]
            avg_ore = np.mean(prices_nok) * 100  # NOK/kWh → øre/kWh
            records.append({
                "dato": current,
                "pris_ore_kwh": round(avg_ore, 1),
            })
        except Exception as e:
            errors += 1
            if errors <= 5 or errors % 50 == 0:
                print(f"  Mangler data for {current}: {e}")

        current += datetime.timedelta(days=1)
        time.sleep(0.05)

    print(f"  Hentet {len(records)} dager ({errors} manglende)")
    return pd.DataFrame(records)


def hent_vaerdata(start, slutt, client_id):
    """Henter daglig temperatur, vind og nedbør fra Frost API (SN18700)."""
    frost_endpoint = "https://frost.met.no/observations/v0.jsonld"
    frost_params = {
        "sources": "SN18700",
        "elements": ",".join([
            "mean(air_temperature P1D)",
            "mean(wind_speed P1D)",
            "sum(precipitation_amount P1D)",
        ]),
        "referencetime": f"{start}/{slutt + datetime.timedelta(days=1)}",
    }

    r = requests.get(frost_endpoint, frost_params, auth=(client_id, ""))
    if r.status_code != 200:
        print(f"  FEIL: Frost API svarte med status {r.status_code}")
        print(f"  {r.text[:500]}")
        sys.exit(1)

    rows = []
    for obs in r.json()["data"]:
        dato = datetime.date.fromisoformat(obs["referenceTime"][:10])
        row = {"dato": dato}
        for el in obs["observations"]:
            eid = el["elementId"]
            val = el["value"]
            if "air_temperature" in eid:
                row["temperatur"] = val
            elif "wind_speed" in eid:
                row["vindstyrke"] = val
            elif "precipitation" in eid:
                row["nedbor"] = val
        rows.append(row)

    df = pd.DataFrame(rows)
    # Kan ha duplikater per dag (ulike timeOffset), ta gjennomsnitt
    df = df.groupby("dato").mean(numeric_only=True).reset_index()
    return df


def hent_magasindata(start_year, end_year):
    """Henter ukentlig magasinfylling for NO1 fra NVE.

    Bruker HentOffentligData som returnerer all historisk data.
    Filtrerer på omrType='EL' og omrnr=1 (NO1).
    """
    url = ("https://biapi.nve.no/magasinstatistikk/api/"
           "Magasinstatistikk/HentOffentligData")

    print("  Henter all historisk magasindata fra NVE...")
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "HON2200-dataset-script/1.0")
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())

    records = []
    for entry in data:
        # Filtrer på EL-område nr 1 (= NO1)
        if entry.get("omrType") != "EL" or entry.get("omrnr") != 1:
            continue
        year = entry.get("iso_aar")
        week = entry.get("iso_uke")
        fyll = entry.get("fyllingsgrad")
        if year is None or week is None or fyll is None:
            continue
        if year < start_year or year > end_year:
            continue
        try:
            week_date = datetime.date.fromisocalendar(year, week, 1)
            records.append({
                "dato": week_date,
                "magasingrad": round(fyll * 100, 1),  # 0.51 → 51.0 %
            })
        except (ValueError, TypeError):
            pass

    return pd.DataFrame(records)


def main():
    rng = np.random.RandomState(SEED)

    # ----------------------------------------------------------
    # 1. Hent strømpriser
    # ----------------------------------------------------------
    print("=" * 60)
    print("1/6  Strømpriser fra hvakosterstrommen.no (NO1)")
    print("=" * 60)

    df_pris = hent_strompriser(START_DATE, END_DATE)
    print(f"  Totalt: {len(df_pris)} dager med prisdata\n")

    # ----------------------------------------------------------
    # 2. Hent værdata fra Frost API
    # ----------------------------------------------------------
    print("=" * 60)
    print("2/6  Værdata fra Frost API (Blindern, SN18700)")
    print("=" * 60)

    if FROST_CLIENT_ID == "SETT_INN_DIN_FROST_CLIENT_ID":
        print("  FEIL: Du må sette FROST_CLIENT_ID.")
        print("  Eksempel: FROST_CLIENT_ID=abc123 python create_dataset.py")
        print("  Registrer gratis på https://frost.met.no/howto.html")
        sys.exit(1)

    df_vaer = hent_vaerdata(START_DATE, END_DATE, FROST_CLIENT_ID)
    print(f"  Hentet værdata for {len(df_vaer)} dager\n")

    # ----------------------------------------------------------
    # 3. Hent magasindata fra NVE
    # ----------------------------------------------------------
    print("=" * 60)
    print("3/6  Magasindata fra NVE (NO1)")
    print("=" * 60)

    df_magasin = hent_magasindata(START_DATE.year, END_DATE.year)
    print(f"  Hentet {len(df_magasin)} ukeverdier\n")

    # ----------------------------------------------------------
    # 4. Merge og beregn features
    # ----------------------------------------------------------
    print("=" * 60)
    print("4/6  Merger datasett og beregner features")
    print("=" * 60)

    df = df_pris.copy()
    df = df.merge(df_vaer, on="dato", how="left")
    df = df.merge(df_magasin, on="dato", how="left")
    df = df.sort_values("dato").reset_index(drop=True)

    # Forward-fill magasindata (ukentlig → daglig)
    df["magasingrad"] = df["magasingrad"].ffill()

    # Ukedag
    dag_map = {
        0: "mandag", 1: "tirsdag", 2: "onsdag",
        3: "torsdag", 4: "fredag", 5: "lørdag", 6: "søndag",
    }
    df["ukedag"] = df["dato"].apply(lambda d: dag_map[d.weekday()])

    # Måned og sesong
    df["maaned"] = df["dato"].apply(lambda d: d.month)

    def get_sesong(m):
        if m in (12, 1, 2):
            return "vinter"
        if m in (3, 4, 5):
            return "var"
        if m in (6, 7, 8):
            return "sommer"
        return "host"

    df["sesong"] = df["maaned"].apply(get_sesong)

    # Lag-feature: pris forrige dag
    df["pris_forrige_dag"] = df["pris_ore_kwh"].shift(1)

    # Target: 1 hvis pris > median, 0 ellers
    median_pris = df["pris_ore_kwh"].median()
    df["hoy_pris"] = (df["pris_ore_kwh"] > median_pris).astype(int)

    print(f"  Rader: {len(df)}")
    print(f"  Median pris: {median_pris:.1f} ore/kWh")
    print(f"  Target-balanse: {df['hoy_pris'].value_counts().to_dict()}\n")

    # ----------------------------------------------------------
    # 5. Legg inn manglende verdier (realistisk)
    # ----------------------------------------------------------
    print("=" * 60)
    print("5/6  Legger inn manglende verdier")
    print("=" * 60)

    n = len(df)

    # ~12 % manglende temperatur, ~15 % manglende vind
    temp_nan_mask = rng.random(n) < 0.12
    vind_nan_mask = rng.random(n) < 0.15
    df.loc[temp_nan_mask, "temperatur"] = np.nan
    df.loc[vind_nan_mask, "vindstyrke"] = np.nan

    print(f"  Manglende temperatur: {temp_nan_mask.sum()} ({temp_nan_mask.mean():.0%})")
    print(f"  Manglende vindstyrke: {vind_nan_mask.sum()} ({vind_nan_mask.mean():.0%})")

    magasin_nan = df["magasingrad"].isna().sum()
    print(f"  Manglende magasingrad (naturlig, fra ukentlig merge): {magasin_nan}")

    pris_lag_nan = df["pris_forrige_dag"].isna().sum()
    print(f"  Manglende pris_forrige_dag (første rad): {pris_lag_nan}\n")

    # ----------------------------------------------------------
    # 6. Konverter dato til streng og lagre
    # ----------------------------------------------------------
    print("=" * 60)
    print("6/6  Lagrer datasett")
    print("=" * 60)

    df["dato"] = df["dato"].apply(lambda d: d.strftime("%Y-%m-%d"))

    output_cols = [
        "dato", "ukedag", "maaned", "sesong",
        "pris_ore_kwh", "temperatur", "vindstyrke", "nedbor",
        "magasingrad", "pris_forrige_dag", "hoy_pris",
    ]

    df_out = df[output_cols]

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    df_out.to_csv(OUTPUT_FILE, index=False)

    print(f"  Lagret til: {OUTPUT_FILE}")
    print(f"  Rader:      {len(df_out)}")
    print(f"  Kolonner:   {list(df_out.columns)}")
    print("\nFerdig!")


if __name__ == "__main__":
    main()
