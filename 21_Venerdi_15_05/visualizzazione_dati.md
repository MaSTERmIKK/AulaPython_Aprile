# 📊 Visualizzazione dei Dati in Python

---

## 1. Perché Visualizzare i Dati?

Prima di scrivere una sola riga di codice, è importante chiedersi: **qual è lo scopo del mio grafico?**

Esistono tre finalità principali:

| Finalità | Descrizione | Quando usarla |
|---|---|---|
| **Informativa** | Fornisce dati chiari e precisi a supporto di decisioni | Report, dashboard |
| **Esplorativa** | Aiuta a scoprire pattern, correlazioni e anomalie nei dati | Analisi iniziale |
| **Narrativa** | Racconta una storia o presenta una sequenza di risultati | Presentazioni, articoli |

> **Regola d'oro:** definisci sempre lo scopo prima di scegliere il tipo di grafico.

---

## 2. Quale Grafico Scegliere?

La scelta del grafico dipende dal **tipo di dati** e dall'**informazione** che vuoi trasmettere.

| Tipo di Dato | Grafici Consigliati |
|---|---|
| Dati categorici | Bar chart, pie chart, diagramma a mosaico |
| Dati continui | Line chart, area chart, scatter plot |
| Distribuzioni | Istogramma, box plot, violin plot |
| Correlazioni | Scatter plot, heat map |
| Composizioni | Stacked bar chart, pie chart, area chart |

---

## 3. Installazione e Import

```bash
pip install matplotlib seaborn
```

```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
```

---

## 4. Matplotlib

### 4.1 Come è strutturato Matplotlib

Matplotlib organizza ogni grafico in una **gerarchia di oggetti**:

```
Figure  →  il "foglio" che contiene tutto
  └── Axes  →  il "grafico" vero e proprio (con i dati)
        ├── Axis  →  gli assi numerici (x e y), con scala e etichette
        └── Artist  →  tutto ciò che si vede: linee, testi, forme, legende
```

```python
fig = plt.figure()          # crea il foglio
ax = fig.add_subplot(111)   # aggiunge un grafico al foglio
```

> Una `Figure` può contenere più `Axes` (es. due grafici affiancati).

---

### 4.2 Grafici Base

#### Grafico a Linee

Ideale per mostrare l'andamento nel tempo di una variabile.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure()
plt.plot(x, y)
plt.title('Grafico a Linee')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
```

---

#### Grafico a Barre

Ideale per confrontare valori tra categorie diverse.

```python
import matplotlib.pyplot as plt

categorie = ['A', 'B', 'C', 'D', 'E']
valori    = [3, 7, 2, 5, 8]

plt.figure()
plt.bar(categorie, valori)
plt.title('Grafico a Barre')
plt.xlabel('Categorie')
plt.ylabel('Valori')
plt.show()
```

---

#### Istogramma

Ideale per visualizzare la **distribuzione** di una variabile numerica.

```python
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)  # 1000 valori casuali con distribuzione normale

plt.figure()
plt.hist(data, bins=30)
plt.title('Istogramma')
plt.xlabel('Valori')
plt.ylabel('Frequenza')
plt.show()
```

---

#### Scatter Plot

Ideale per esplorare la **relazione** tra due variabili numeriche.

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(50)
y = np.random.rand(50)

plt.figure()
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
```

---

### 4.3 Configurazione con `rcParams`

`rcParams` è il dizionario globale di Matplotlib che ti permette di impostare uno stile predefinito per tutti i grafici della sessione.

```python
plt.rcParams['figure.figsize'] = [10, 6]   # dimensione predefinita
plt.rcParams['figure.dpi']     = 100       # risoluzione
plt.rcParams['figure.facecolor'] = 'white' # sfondo bianco
```

> Imposta `rcParams` all'inizio del tuo notebook/script per avere grafici consistenti senza ripetere le impostazioni ogni volta.

---

### 4.4 Subplot

I **subplot** ti permettono di visualizzare più grafici in una griglia, affiancati all'interno di una stessa Figure. Questo è utile per confrontare diversi dataset o rappresentazioni dello stesso dataset.

#### Creazione con `plt.subplots()`

Il metodo `plt.subplots(nrows, ncols)` crea una griglia di grafici.

```python
import matplotlib.pyplot as plt
import numpy as np

# Crea una griglia di 2 righe e 2 colonne
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

# axes è un array 2D: puoi accedere ai singoli assi con axes[riga, colonna]

# Primo grafico (in alto a sinistra)
axes[0, 0].plot([1, 2, 3, 4], [1, 4, 2, 3])
axes[0, 0].set_title('Grafico 1: Linee')

# Secondo grafico (in alto a destra)
axes[0, 1].scatter([1, 2, 3, 4], [2, 3, 1, 4])
axes[0, 1].set_title('Grafico 2: Scatter')

# Terzo grafico (in basso a sinistra)
axes[1, 0].bar(['A', 'B', 'C'], [3, 7, 5])
axes[1, 0].set_title('Grafico 3: Barre')

# Quarto grafico (in basso a destra)
axes[1, 1].hist(np.random.randn(100), bins=20)
axes[1, 1].set_title('Grafico 4: Istogramma')

plt.tight_layout()  # regola automaticamente lo spazio tra i grafici
plt.show()
```

---

## 5. Seaborn

### 5.1 Cos'è Seaborn?

Seaborn è costruita **sopra Matplotlib** e offre:

- un'interfaccia più semplice e con meno codice
- integrazione diretta con i **DataFrame pandas**
- grafici statisticamente informativi (con intervalli di confidenza, KDE, ecc.)
- temi visivi già pronti e curati

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

---

### 5.2 Temi Predefiniti

Puoi migliorare l'estetica dei tuoi grafici con una sola riga:

```python
sns.set_theme()                       # tema di default
sns.set_theme(style="whitegrid")      # sfondo bianco con griglia
sns.set_theme(style="darkgrid")       # sfondo scuro con griglia
```

Altri stili disponibili: `dark`, `white`, `ticks`.

---

### 5.3 Grafici con Seaborn

#### Grafico a Barre

Seaborn calcola automaticamente la media e l'intervallo di confidenza.

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")  # dataset di esempio incluso in Seaborn

sns.barplot(x="day", y="total_bill", data=tips)
plt.title('Conto Totale per Giorno')
plt.show()
```

---

#### Grafico a Linee

Gestisce automaticamente più gruppi con `hue` e `style`.

```python
import seaborn as sns
import matplotlib.pyplot as plt

fmri = sns.load_dataset("fmri")

sns.lineplot(x="timepoint", y="signal", data=fmri,
             hue="region", style="event")
plt.title('Segnale FMRI nel Tempo')
plt.show()
```

---

#### Istogramma con KDE

La curva KDE (Kernel Density Estimation) mostra la distribuzione in modo continuo, sovrapposta all'istogramma.

```python
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

sns.histplot(data=penguins, x="flipper_length_mm", kde=True)
plt.title('Distribuzione Lunghezza Pinne dei Pinguini')
plt.show()
```

---

### 5.4 Subplot con Seaborn

Seaborn non ha un metodo nativo per i subplot, ma si integra perfettamente con `plt.subplots()` di Matplotlib: basta passare l'asse (`ax`) desiderato a ciascuna funzione Seaborn tramite il parametro `ax`.

#### Esempio Base: Grafici Affiancati

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")
tips = sns.load_dataset("tips")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Grafico 1: distribuzione del conto totale
sns.histplot(data=tips, x="total_bill", kde=True, ax=axes[0])
axes[0].set_title('Distribuzione del Conto Totale')

# Grafico 2: conto totale per giorno
sns.barplot(data=tips, x="day", y="total_bill", ax=axes[1])
axes[1].set_title('Conto Totale per Giorno')

plt.tight_layout()
plt.show()
```

---

### 5.5 Matplotlib vs Seaborn — Quando usare quale?

| | Matplotlib | Seaborn |
|---|---|---|
| Controllo | Totale | Parziale (ma personalizzabile) |
| Semplicità | Più verboso | Meno codice |
| Integrazione pandas | Manuale | Diretta |
| Grafici statistici | Da costruire a mano | Già inclusi |

> **Consiglio pratico:** usa Seaborn per l'analisi esplorativa e Matplotlib quando hai bisogno di personalizzazioni molto precise.

---

## 6. Esercizi

### Esercizio 1 — Statistiche di Base

Genera un DataFrame pandas con una colonna `temperature` (30 valori casuali) e calcola:

- temperatura massima
- temperatura minima
- temperatura media
- mediana delle temperature

```python
import pandas as pd
import numpy as np

# Genera i dati
np.random.seed(42)
df = pd.DataFrame({'temperature': np.random.uniform(10, 35, 30)})

# Calcola le statistiche
print("Max:   ", df['temperature'].max())
print("Min:   ", df['temperature'].min())
print("Media: ", df['temperature'].mean())
print("Mediana:", df['temperature'].median())
```

---

### Esercizio 2 — Normalizzazione Min-Max

Crea un DataFrame con colonne `altezza`, `peso` ed `età`. Applica la normalizzazione min-max ad `altezza` e `peso` (scala i valori tra 0 e 1), lasciando `età` invariata.

```python
import pandas as pd
import numpy as np

# Dati di esempio
df = pd.DataFrame({
    'altezza': [160, 175, 182, 158, 170],
    'peso':    [55,  80,  90,  50,  70],
    'eta':     [25,  30,  22,  28,  35]
})

df_norm = df.copy()

# Normalizzazione min-max
for col in ['altezza', 'peso']:
    df_norm[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

print("Originale:\n", df)
print("\nNormalizzato:\n", df_norm)
```

---

### Esercizio 3 — Serie Temporale con NumPy + pandas + Matplotlib

Genera 365 giorni di visitatori in un parco, con trend crescente. Poi:

1. Crea un DataFrame con date come indice
2. Calcola media e deviazione standard mensile
3. Traccia il grafico giornaliero con media mobile a 7 giorni
4. Traccia la media mensile

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Genera i dati
np.random.seed(0)
giorni      = 365
trend       = np.linspace(0, 500, giorni)             # crescita graduale
visitatori  = np.random.normal(2000, 500, giorni) + trend
date        = pd.date_range(start='2024-01-01', periods=giorni)

# 2. Crea il DataFrame
df = pd.DataFrame({'visitatori': visitatori}, index=date)

# 3. Statistiche mensili
mensile = df.resample('ME').agg(['mean', 'std'])
print(mensile)

# 4. Grafico giornaliero con media mobile
df['media_mobile_7g'] = df['visitatori'].rolling(7).mean()

plt.figure(figsize=(12, 4))
plt.plot(df.index, df['visitatori'], alpha=0.4, label='Giornaliero')
plt.plot(df.index, df['media_mobile_7g'], color='red', label='Media mobile 7gg')
plt.title('Visitatori Giornalieri — Parco')
plt.xlabel('Data')
plt.ylabel('Visitatori')
plt.legend()
plt.tight_layout()
plt.show()

# 5. Grafico media mensile
plt.figure(figsize=(10, 4))
plt.bar(mensile.index.strftime('%b'), mensile[('visitatori', 'mean')])
plt.title('Media Mensile Visitatori')
plt.xlabel('Mese')
plt.ylabel('Media visitatori')
plt.tight_layout()
plt.show()
```

---

## Riepilogo

```
Visualizzazione dei Dati
├── Scopo: informativo / esplorativo / narrativo
├── Scelta del grafico in base al tipo di dato
├── Matplotlib
│   ├── Architettura: Figure → Axes → Axis → Artist
│   ├── Grafici: line, bar, hist, scatter
│   └── Configurazione globale con rcParams
└── Seaborn
    ├── Costruita su Matplotlib, interfaccia più semplice
    ├── Integrazione diretta con pandas
    ├── Temi predefiniti (set_theme)
    └── Grafici: barplot, lineplot, histplot + KDE
```
