# HON2200 Planlegging vår 2026

**Dato:** 2026-01-16
**Ansvarlig:** Henrik Sveinsson

## Bakgrunn

Denne planleggingen er gjort i forkant av vår 2026-semesteret, basert på:
1. [TP-timeplan for v26](https://tp.educloud.no/uio/timeplan/timeplan.php?id%5B%5D=HON2200%2C1&type=course&sem=26v&hide_old=1)
2. [Emnebeskrivelse](https://www.uio.no/studier/emner/matnat/fys/HON2200/)
3. Emneevaluering fra v25 (se `evalueringer/evaluering_v25.md`)

## Hovedendringer for v26

### 1. Ny timeplan

Digital etikk flyttes fra uke 8-9 til uke 5-6 (basert på TP-timeplan med Aksel Sterri).

| Uke | Dato | Innhold |
|-----|------|---------|
| 1 | 23. jan | Introduksjon til Pandas |
| 2 | 30. jan | Lineær regresjon |
| 3 | 6. feb | Logistisk regresjon |
| 4 | 13. feb | Kryssvalidering, overtrening |
| **5** | **20. feb** | **Digital etikk** (+ Aksel Sterri) |
| **6** | **27. feb** | **Digital etikk** (+ Aksel Sterri) |
| 7 | 6. mar | Beslutningstrær |
| 8 | 13. mar | Random forest, one-hot encoding |
| **9** | **20. mar** | **Prosjekt 1 oppstart** |
| - | 23. mar (ma) | Orakeltjeneste |
| 10 | 27. mar | Prosjektveiledning |
| - | 3. apr | *Langfredag - ingen undervisning* |
| 11 | 10. apr | Prosjektveiledning |
| 12 | 17. apr | Prosjektveiledning |
| 13 | 24. apr | Prosjekt 2 oppstart |
| 14 | 8. mai | Prosjektveiledning |
| 15 | 15. mai | Siste veiledning |
| 16 | 22. mai | Oppsummering |

**Begrunnelse for prosjekt 1 i uke 9:** Langfredag 3. april betyr at uke 10 (27. mars) er rett før påskeferie. Ved å starte prosjekt 1 i uke 9 får studentene orakeltjeneste mandag 23. mars og veiledning fredag 27. mars før påskeferien.

### 2. Nye LLM-skrevne supplementsmaterialer

Basert på tilbakemelding fra v25-evalueringen om at videoer er "svært lærerike" og at live-koding "går for fort", lages alternative forklaringer i notebook-format.

Nye notebooks i `lectures/llm/`:
- `llm_01_pandas.ipynb` - Pandas introduksjon
- `llm_02_linreg.ipynb` - Lineær regresjon
- `llm_03_logreg.ipynb` - Logistisk regresjon
- `llm_04_kryssvalidering.ipynb` - Kryssvalidering
- `llm_05_beslutningstraer.ipynb` - Beslutningstrær
- `llm_06_ensemble.ipynb` - Ensemble-metoder
- `llm_07_onehot.ipynb` - One-hot encoding

### 3. Opprydding i repository

- Sletter Quarto-genererte `*_files/` mapper
- Arkiverer gamle live-notebooks til `lectures/gamle_live_notebooks/`
- Arkiverer innhold i `tmp/`

## Evidens fra v25-evaluering

### Nøkkelfunn

| Tema | Funn | Tiltak |
|------|------|--------|
| Videoer | "Svært lærerike, kan spoles/repeteres" | Lager video for kryssvalidering |
| Live-koding | "Tempoet gikk for fort" | LLM-notebooks som supplement |
| Ferdighetssprik | MN: 2-5 t/uke, SV/HF: 10-12 t/uke | Pandas-intro med fokus på grunnleggende |
| Forkunnskaper | "Spranget fra HON2110 for stort" | Brobygging i starten |

### Sitater fra evaluering

> "Videoer der lærer koder og forklarer samtidig var svært lærerike for å lære anvendelse i Python (kan spoles/repeteres, får med detaljene). Ønske om flere slike videoer."

> "I klasserommet gikk kodingstempoet for fort for de med lite forkunnskaper, man falt lett av."

## Forventet effekt

1. **Bedre fleksibilitet:** Studenter kan arbeide i eget tempo med LLM-notebooks
2. **Utjevning:** Svakere studenter får mer støttemateriale
3. **Forberedelse til påske:** Prosjekt 1 oppstart før påskeferie gir mer sammenhengende arbeidstid

## Oppfølging

Effekten evalueres gjennom:
- Midtveisevaluering (nettskjema)
- Sluttevaluering
- Observasjon av studentprestasjoner på oblig og prosjekt
