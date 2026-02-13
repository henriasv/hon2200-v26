# Videomanus: Kryssvalidering og overtrening

**Varighet:** Ca. 30 minutter
**Format:** Skjermopptak med koding og forklaring
**Målgruppe:** HON2200-studenter (tverrfaglig, varierende programmeringsbakgrunn)

---

## Del 1: Introduksjon (3 min)

### Manus

> Hei og velkommen til denne videoen om kryssvalidering. Jeg er [navn], og i dag skal vi snakke om et av de viktigste konseptene innen maskinlæring: Hvordan vet vi om modellen vår faktisk er god?
>
> Det høres kanskje enkelt ut - bare se hvor godt modellen passer dataene, ikke sant? Men som vi skal se, er det faktisk en felle her som mange faller i.
>
> I denne videoen skal vi:
> 1. Først se på et eksempel som viser problemet med overtrening
> 2. Så lære om train-test split
> 3. Deretter k-fold kryssvalidering
> 4. Og til slutt bruke dette til å velge mellom ulike modeller

### Skjermvisning

- Tittelslide med innhold
- Åpne Jupyter notebook

---

## Del 2: Problemet med overtrening (7 min)

### Manus

> La oss starte med å lage noen data. Jeg skal generere punkter fra en sinuskurve, men med litt støy - som om vi har gjort målinger med litt usikkerhet.

**[Skriv kode:]**
```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n = 30
x = np.sort(np.random.uniform(0, 2*np.pi, n))
y_true = np.sin(x)
y = y_true + np.random.normal(0, 0.3, n)

plt.scatter(x, y)
plt.plot(x, y_true, 'g--', label='Sann funksjon')
plt.legend()
plt.show()
```

> Nå skal vi tilpasse polynomer til disse dataene. La oss starte med en rett linje - et førstegradspolynom.

**[Skriv kode:]**
```python
koeff1 = np.polyfit(x, y, 1)
y_pred1 = np.polyval(koeff1, x)

plt.scatter(x, y)
plt.plot(x, y_pred1, 'r-')
plt.title('Grad 1 polynom')
plt.show()
```

> En rett linje fanger ikke opp krumningen. La meg prøve et høyere polynom.

**[Vis grad 3, 10, og 25 polynomer]**

> Se på dette. Grad 25-polynomet går gjennom nesten hvert eneste punkt! Men... ser det ut som en god modell?
>
> La oss beregne feilen - mean squared error - for hvert polynom.

**[Skriv kode som beregner MSE for alle grader]**

> Interessant! Treningsfeilen synker hele veien. Grad 25 har nesten null feil. Men dette er et problem - for dette polynomet har lært *støyen*, ikke bare den underliggende sammenhengen.
>
> Dette kalles **overtrening** eller **overfitting**. Modellen er så fleksibel at den tilpasser seg tilfeldigheter i dataene, ikke bare det systematiske mønsteret.

### Nøkkelpunkt å fremheve

- Vise at treningsfeil alltid synker med mer kompleks modell
- "Grad 25 polynom er som å pugge til eksamen uten å forstå"

---

## Del 3: Treningsfeil vs. Testfeil (5 min)

### Manus

> Problemet er at vi evaluerer modellen på de *samme* dataene vi trente på. Det er som å gi noen fasit på prøven og spørre "hvor godt kan du dette?".
>
> La meg generere helt nye testdata.

**[Skriv kode:]**
```python
x_test = np.sort(np.random.uniform(0, 2*np.pi, 30))
y_test = np.sin(x_test) + np.random.normal(0, 0.3, 30)
```

> Nå kan vi beregne feilen på *nye* data som modellen aldri har sett.

**[Skriv kode som beregner test-feil for alle grader]**

**[Plott både trenings- og testfeil]**

> Se på dette! Treningsfeilen synker hele tiden, men testfeilen går *opp* etter et visst punkt.
>
> Det optimale er der hvor testfeilen er lavest - ikke der treningsfeilen er lavest.
>
> Dette er den grunnleggende innsikten: En modell som er *for god* på treningsdata, er ofte *dårlig* på nye data.

### Nøkkelpunkt

- Tegne på skjermen: U-formet kurve for testfeil
- "Sweet spot" mellom underfitting og overfitting

---

## Del 4: Train-Test Split (5 min)

### Manus

> OK, så vi må evaluere på data modellen ikke har sett. Den enkleste metoden er å dele dataene våre i to: treningssett og testsett.

**[Skriv kode:]**
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    x.reshape(-1,1), y, test_size=0.3, random_state=42
)
```

> Her holder vi tilbake 30% av dataene som testsett. Vi trener kun på de resterende 70%.
>
> La meg visualisere dette.

**[Plott med ulike farger for trening og test]**

> Men det er et problem: Resultatet avhenger av *hvilke* punkter som havner i test vs. trening. Se hva som skjer hvis jeg endrer random_state.

**[Vis at optimal grad varierer med random_state]**

> Noen ganger er grad 3 best, noen ganger grad 5. Hvordan kan vi få et mer robust svar?

### Nøkkelpunkt

- Demonstrere variasjon i resultater
- "En enkelt train-test split er som å trekke ett kort fra en kortstokk"

---

## Del 5: K-Fold Kryssvalidering (8 min)

### Manus

> Løsningen er **kryssvalidering**. I stedet for én tilfeldig oppdeling, gjør vi mange.
>
> K-fold kryssvalidering fungerer slik:
> 1. Del dataene i K like store deler - vi kaller dem "folds"
> 2. For hver fold: bruk den som testsett, og de andre K-1 som treningssett
> 3. Beregn testfeil for hver
> 4. Ta gjennomsnittet

**[Tegn diagram som viser 5-fold]**

> La oss implementere dette fra scratch.

**[Skriv kode:]**
```python
from sklearn.model_selection import KFold

kf = KFold(n_splits=5, shuffle=True, random_state=42)

for fold, (train_idx, test_idx) in enumerate(kf.split(x)):
    print(f"Fold {fold+1}: Trening={len(train_idx)}, Test={len(test_idx)}")
```

> Nå skal jeg lage en funksjon som gjør kryssvalidering for polynomregresjon.

**[Skriv fullstendig CV-funksjon]**

**[Kjør for alle polynomgrader og plott]**

> Se - nå får vi et mye mer stabilt svar. Og vi kan til og med beregne usikkerheten ved å se på standardavviket mellom foldene.

### Nøkkelpunkt

- Animasjon/diagram som viser roterende testsett
- "Hver observasjon er testsett nøyaktig én gang"

---

## Del 6: Scikit-learn sin cross_val_score (3 min)

### Manus

> I praksis trenger vi ikke implementere dette selv. Scikit-learn har `cross_val_score`.

**[Skriv kode:]**
```python
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

def lag_modell(grad):
    return make_pipeline(
        PolynomialFeatures(grad),
        LinearRegression()
    )

modell = lag_modell(3)
scores = cross_val_score(modell, x.reshape(-1,1), y, 
                         cv=5, scoring='neg_mean_squared_error')
print(-scores.mean())
```

> Merk at scikit-learn returnerer *negative* MSE fordi de vil at høyere score skal være bedre.

---

## Del 7: Bias-Variance Tradeoff (3 min)

### Manus

> La meg avslutte med å forklare *hvorfor* vi ser denne U-formen i testfeil.
>
> Feilen kan deles i tre komponenter:
> - **Bias**: Hvor langt unna sann verdi er modellen i gjennomsnitt?
> - **Varians**: Hvor mye varierer modellen mellom ulike treningssett?
> - **Irreducible error**: Støy vi aldri kan forklare
>
> Enkle modeller har høy bias (for stiv til å fange mønsteret) men lav varians.
> Komplekse modeller har lav bias men høy varians (ustabile).

**[Vis bias-variance tradeoff-figur]**

> Det optimale er balansen mellom disse - og kryssvalidering hjelper oss finne den.

---

## Del 8: Oppsummering (2 min)

### Manus

> La meg oppsummere det viktigste:
>
> 1. **Aldri evaluer på treningsdata** - du vil undervurdere feilen
> 2. **Train-test split** er enkelt, men resultatet avhenger av oppdelingen
> 3. **K-fold kryssvalidering** gir et robust estimat ved å bruke alle data som testsett
> 4. **Bruk kryssvalidering til modellvalg** - finn den modellen som generaliserer best
>
> Husk: Målet med maskinlæring er ikke å lære *treningsdataene* perfekt, men å lære *mønsteret* som generaliserer til nye data.
>
> Lykke til med øvelsene, og send gjerne spørsmål på diskusjonsforumet!

---

## Tekniske notater for innspilling

### Forberedelser
- Ha ferdig notebook med alle kodeceller forberedt (men skjult)
- Test at alle plots vises riktig
- Zoom på kode når du skriver

### Tips
- Pause ofte for å la studenter tenke
- Gjenta nøkkelbegreper
- Bruk markør for å peke på viktige ting i plots

### Filnavn for medfølgende notebook
`video_kryssvalidering_kode.qmd`
