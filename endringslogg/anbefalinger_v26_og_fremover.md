# Anbefalinger til videreutvikling av HON2200

**Dato:** 2026-01-16
**Forfatter:** LLM-assistent (basert på gjennomgang av kursmaterialer og evalueringer)
**Til:** Henrik Sveinsson

---

## Sammendrag

Dette dokumentet gir anbefalinger for videreutvikling av HON2200 basert på:
- Gjennomgang av eksisterende kursmaterialer
- Emneevaluering v25
- Analyse av ferdighetsgap mellom fakulteter
- Sammenligning med læringsmål i emnebeskrivelsen

Anbefalingene er kategorisert etter prioritet og ressurskrav.

---

## Høy prioritet (anbefales implementert v26/v27)

### 1. Bro-økter i starten av semesteret

**Problem:** "Spranget fra HON2110 er for stort" - mange studenter mangler forkunnskaper i programmering og matematikk.

**Anbefaling:**
- Dediker de første 45 minuttene av forelesning 1 til en "Python-oppfrisking"
- Fokus på: variabler, lister, løkker, funksjoner, feilsøking
- Gi en diagnostisk quiz (ikke tellende) for å identifisere studenter som trenger ekstra støtte
- Lag en "ressursside" med lenker til grunnleggende Python-materiale

**Ressurskrav:** Lav-moderat (én gang)

### 2. Differensiert materiale for ulike nivåer

**Problem:** MN-studenter bruker 2-5 timer/uke, SV/HF bruker 10-12 timer. Kodingstempoet i timen "går for fort".

**Anbefaling:**
- Marker øvingsoppgaver med vanskelighetsgrad: ⭐ (grunnleggende), ⭐⭐ (middels), ⭐⭐⭐ (utfordrende)
- Lag "minimumskrav"-oppgaver som alle må klare
- Lag "utvidede oppgaver" for de som vil gå dypere
- Bruk LLM-notebookene som supplement for de som trenger mer forklaring

**Ressurskrav:** Lav (kan gjøres gradvis)

### 3. Flere videoressurser

**Problem:** "Videoer der lærer koder og forklarer samtidig var svært lærerike ... kan spoles/repeteres ... Ønske om flere slike videoer."

**Anbefaling:**
- Prioriter video for de mest konseptuelt krevende temaene:
  1. **Kryssvalidering** (manus allerede laget)
  2. **Logistisk regresjon** - sigmoid-funksjonen og tolkning
  3. **Feature importance** - hva betyr det egentlig?
- Korte videoer (10-15 min) er bedre enn lange
- Legg inn "pause her og prøv selv"-punkter

**Ressurskrav:** Høy (tidkrevende å produsere)

### 4. Strukturert AI-opplæring

**Problem:** "Mange studenter bruker språkmodeller ... men vi har ikke hatt noen eksplisitt trening i bruk av AI til koding."

**Anbefaling:**
- Lag en dedikert økt (30-45 min) om "AI-assistert koding"
- Innhold:
  - Når er AI nyttig? (feilsøking, forklare kode, generere startkode)
  - Når er AI farlig? (blindt kopiere uten forståelse)
  - Øvelse: Sammenligne egen løsning med AI-løsning
  - Diskusjon: Etiske aspekter ved AI-bruk i akademisk arbeid
- Integrer dette naturlig før prosjektarbeidet starter

**Ressurskrav:** Moderat (én gang)

---

## Middels prioritet (vurder for v27)

### 5. Tydeligere progresjonsplan fra HON2110

**Problem:** "Koordinering på tvers av undervisere i Honours (felles begrepsbruk/fremgangsmåter)."

**Anbefaling:**
- Lag et dokument som viser forventet ferdighetsnivå ved start av HON2200
- Del dette med HON2110-undervisere
- Vurder å legge inn et "pre-test" som studenter gjør før semesterstart
- Identifiser konkrete konsepter som bør dekkes i HON2110

**Ressurskrav:** Moderat (koordinering)

### 6. Forbedret gruppedynamikk

**Problem:** "Gruppedynamikk var svært variabel ... noen opplevde gruppene var litt 'lotto'."

**Anbefaling:**
- Introduser enkle rolleavklaringer i gruppene (f.eks. prosjektleder, kodeansvarlig, skriveansvarlig)
- Lag en "gruppekontrakt"-mal som gruppene fyller ut ved oppstart
- Vurder korte ukentlige statusmøter (5 min) med hver gruppe
- Gi konkrete tips om parprogrammering

**Ressurskrav:** Lav

### 7. Styrke statistisk forståelse

**Problem:** "Styrk opplæring i tolkning/konklusjoner og grunnleggende statistiske begreper (f.eks. statistisk signifikans)."

**Anbefaling:**
- Legg til en kort modul om:
  - Statistisk signifikans vs. praktisk signifikans
  - Korrelasjon vs. kausalitet
  - Konfidensintervaller (intuitiv forklaring)
- Bruk konkrete eksempler fra medieoppslag som mistolker statistikk
- Koble dette til prosjektarbeidet

**Ressurskrav:** Moderat

---

## Lavere prioritet (langsiktige forbedringer)

### 8. Interaktive elementer i forelesninger

**Anbefaling:**
- Vurder bruk av Mentimeter eller lignende for korte avstemninger
- "Predict what happens"-øvelser før kode kjøres
- Felles debugging-økter der alle prøver å finne feilen

### 9. Alumni-besøk

**Anbefaling:**
- Inviter tidligere HON2200-studenter til å dele hvordan de har brukt ferdighetene
- Korte innlegg (10-15 min) om relevans for arbeidslivet

### 10. Automatisert tilbakemelding

**Anbefaling:**
- Vurder bruk av nbgrader eller lignende for automatisk sjekk av kodeoppgaver
- Gir umiddelbar tilbakemelding og avlaster seminarlærer

---

## Konkrete forbedringer til eksisterende materiale

### Forelesning 1: Pandas

**Observasjon:** God intro, men kan være overveldende for nybegynnere.

**Anbefaling:**
- Start med "hvorfor trenger vi Pandas?" - motiverende eksempel
- Vis forskjellen på å gjøre noe med rå Python vs. Pandas
- Reduser antall nye konsepter - fokus på det mest essensielle

### Forelesning 4: Kryssvalidering

**Observasjon:** Kritisk konsept som mange sliter med.

**Anbefaling:**
- Bruk mer tid på å bygge intuisjon før formler
- Visuell demonstrasjon av "hvorfor treningsfeil lyver"
- Koble til hverdagseksempler: "Det er som å pugge fasit"

### Obligatorisk oppgave (Titanic)

**Observasjon:** God oppgave, men kan være for åpen for de usikre.

**Anbefaling:**
- Legg til en "steg-for-steg"-guide for de som trenger det
- Marker tydelig: "Minimum forventet" vs. "For de som vil utfordre seg"

---

## Måling av effekt

For å evaluere om endringene har ønsket effekt, anbefales:

| Tiltak | Måling |
|--------|--------|
| Bro-økter | Pre/post diagnostisk test |
| Differensiert materiale | Spørsmål i midtveisevaluering |
| Videoressurser | Visningstall + studenttilfredshet |
| AI-opplæring | Observasjon av AI-bruk i prosjekter |
| Gruppedynamikk | Spørsmål om arbeidsfordeling i sluttevaluering |

---

## Oppsummering: Anbefalt prioritering for v26

1. ✅ **Gjennomført:** LLM-skrevne supplementer, ny timeplan, video-manus
2. 🎯 **Prioriter:** Bro-økt i forelesning 1, differensierte oppgaver
3. 📹 **Produser:** Video om kryssvalidering (manus klart)
4. 🤖 **Planlegg:** AI-opplæringsøkt før prosjekt 1

---

## Referanser

- Emneevaluering HON2200 v25
- TP-timeplan v26
- SOTL-prinsipper for evidensbasert undervisningsutvikling
