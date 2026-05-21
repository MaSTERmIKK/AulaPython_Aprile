# Esame Finale — Python per l'Analisi dei Dati

---

## Scenario: *VeloCittà Analytics*

Sei un analista junior di **VeloCittà**, startup italiana di bike sharing attiva a Milano, Roma e Torino. Costruisci un sistema di analisi end-to-end che copra OOP, SQL teorico, NumPy, Pandas e visualizzazione.

---

## Task 1 — Setup & Python Base

>**1.1 — Repository GitHub**

- Crea il repo `velocita-analytics` con la struttura sopra
- Il `README.md` deve includere: titolo, descrizione (3-5 righe), istruzioni di esecuzione

**1.2 — Funzioni di utilità**

Scrivi queste tre funzioni **senza librerie esterne**:

- `calcola_durata_minuti(ora_inizio: str, ora_fine: str) -> int`
  - Formato input: `"HH:MM"`
  - Solleva `ValueError` se `ora_fine` è precedente a `ora_inizio`

- `classifica_corsa(durata_minuti: int) -> str`
  - `"breve"` se < 15 min, `"media"` se 15–45 min, `"lunga"` se > 45 min

- `riepilogo_corse(lista_durate: list) -> dict`
  - Chiavi restituite: `totale`, `media`, `max`, `min`, `brevi`, `medie`, `lunghe`

---

## Task 2 — OOP Parte 1: Record e Dataset

**2.1 — Classe `Bicicletta`** — pattern Record

Attributi nel `__init__`:

- `id_bici: str` — es. `"MI-042"`
- `tipo: str` — `"classica"` o `"elettrica"`
- `stazione_corrente: str`
- `km_percorsi: float`
- `disponibile: bool`

Metodi obbligatori:

- `noleggia(self, utente: str) -> str` — imposta `disponibile = False`; solleva `ValueError` se già in uso
- `restituisci(self, stazione: str, km_aggiunta: float) -> None` — aggiorna stazione e km
- `__str__` — es. `"[MI-042] elettrica | Cadorna | 342.5 km | ✓ disponibile"`
- `__repr__`

**2.2 — Classe `FlottaBici`** — pattern Dataset

Attributi:

- `biciclette: list`
- `citta: str`

Metodi obbligatori:

- `aggiungi(self, bici: Bicicletta) -> None`
- `rimuovi(self, id_bici: str) -> None` — solleva `KeyError` se non trovata
- `cerca_per_id(self, id_bici: str) -> Bicicletta` — solleva `KeyError` se non trovata
- `disponibili(self) -> list`
- `statistiche(self) -> dict` — chiavi: `totale`, `disponibili`, `in_uso`, `km_totali_flotta`, `km_medi_per_bici`
- `__len__`
- `@classmethod da_lista(cls, citta: str, dati: list) -> "FlottaBici"` — costruisce la flotta da una lista di dizionari con chiavi `id`, `tipo`, `stazione`, `km`

---

## Task 3 — OOP Parte 2: Ereditarietà, Incapsulamento, Polimorfismo

>**3.1 — Ereditarietà**

Crea due sottoclassi di `Bicicletta`:

`BiciclettaClassica(Bicicletta)`:

- Aggiunge attributo `taglia: str` (`"S"`, `"M"`, `"L"`)
- Override di `__str__` per includere la taglia

`BiciclettaElettrica(Bicicletta)`:

- Aggiunge attributo `batteria_percentuale: int` (0–100)
- Aggiunge `ricarica(self, percentuale: int) -> None` (massimo 100)
- Override di `__str__` per mostrare livello batteria, es. `🔋 78%`
- Override di `noleggia` — solleva `ValueError` se `batteria_percentuale < 20`

>*Aggiungi anche una o più sottoclassi a tua scelta*
---
>**3.2 — Incapsulamento**

- Rinomina `km_percorsi` → `_km_percorsi`
- Crea `@property km_percorsi` in sola lettura
- Crea `aggiungi_km(self, km: float) -> None` — valida che `km > 0` prima di aggiornare

>*Aggiungi anche una o più esempi di incapsulamento a tua scelta*
---
>**3.3 — Polimorfismo**

Realizza una piccola dimostrazione di polimorfismo:

```python
def stampa_flotta(biciclette: list) -> None:
    ...
```

- Crea una lista con oggetti di almeno 2 classi diverse del dominio
- Applica la stessa operazione a tutti gli elementi senza fare controlli espliciti sul tipo
- Inserisci un commento breve (2-3 righe) in cui spieghi l'idea di interfaccia comune e dispatch dinamico
- Mostra anche una chiamata di esempio della funzione

>*Aggiungi dimostrazioni del polimorfismo a tua scelta*
---

---

## Task 4 — SQL Teorico

> Solo query SQL e spiegazioni testuali. Nessun codice Python.

Tabelle disponibili:

```sql
corse(id_corsa, id_bici, id_utente, stazione_partenza, stazione_arrivo,
      data_corsa, durata_minuti, km_percorsi)
biciclette(id_bici, tipo, citta, stazione_corrente, km_totali)
utenti(id_utente, nome, citta, tipo_abbonamento, data_iscrizione)
stazioni(id_stazione, nome, citta, n_posti, latitudine, longitudine)
```

Per ogni domanda scrivi: la query SQL + una spiegazione di 1-3 righe.

- **D1**  — Tutte le corse a Milano ordinate per data decrescente. Mostra: `id_corsa`, `id_bici`, `data_corsa`, `durata_minuti`.
- **D2**  — Quante bici elettriche per ogni città? Ordina dalla città con più bici a quella con meno.
- **D3**  — Durata media, massima e minima per tipo di bicicletta. (JOIN richiesto)
- **D4**  — Stazioni di Milano con più di 50 arrivi in aprile 2026. Ordina per conteggio decrescente.
- **D5**  — Utenti `"Premium"` con almeno 10 corse: mostra numero corse totali e km totali. (JOIN richiesto)
- **D6**  — Spiega a parole cosa fa questa query e quale informazione di business produce:

```sql
SELECT
    s.nome AS stazione,
    s.citta,
    COUNT(c_in.id_corsa)  AS arrivi,
    COUNT(c_out.id_corsa) AS partenze,
    COUNT(c_in.id_corsa) - COUNT(c_out.id_corsa) AS bilancio
FROM stazioni s
LEFT JOIN corse c_in  ON s.nome = c_in.stazione_arrivo
LEFT JOIN corse c_out ON s.nome = c_out.stazione_partenza
GROUP BY s.nome, s.citta
ORDER BY bilancio DESC;
```

---

## Task 5 — Analisi Numerica con NumPy

>*Per qualsiasi delle sezioni avete la libertà di aggiungere esempi o funzionalità extra a quelli richiesti*

---

>**5.1 — Generazione dati**

Usa `np.random.seed(42)`, poi crea:

- `durate` — 500 valori interi da distribuzione normale (media 28, std 12); clippa a ≥ 1
- `km` — `durate * np.random.uniform(0.15, 0.25, size=500)`, arrotondati a 2 decimali
- `velocita` — `km / (durate / 60)`

Stampa: shape, dtype e un riepilogo (min, max, media, std) per le tre variabili.

>**5.2 — Slicing e selezione**

- Estrai le prime 10 e le ultime 10 corse (da `durate`)
- Usa **fancy indexing** per selezionare le corse agli indici `[0, 42, 99, 150, 200, 350, 499]`
- Usa una **maschera booleana** per trovare le corse con `durate > 45` e la loro distanza media
- Trova l'indice della corsa con velocità massima e minima

>**5.3 — Statistiche e normalizzazione**

- Calcola i percentili 25°, 50°, 75°, 90° delle durate
- Normalizza `durate` con min-max: `(x - min) / (max - min)`; verifica che i valori siano in [0, 1]
- Calcola la correlazione di Pearson tra `durate` e `km` solo con NumPy; commenta il risultato in una riga

>**5.4 — Serie temporale simulata**

- Genera 30 giorni di corse: `np.random.randint(80, 200, size=30)`
- Calcola la media mobile a 7 giorni
- Individua il giorno con picco massimo e minimo
- Stampa un riepilogo tabellare: giorno, corse, media mobile

---

## Parte 3 — Pandas + Visualizzazione

---

## Task 6 — Pandas: Caricamento, Pulizia e Analisi

>**6.1 — Creazione DataFrame**

Crea tre DataFrame direttamente via codice (no file CSV esterni).

`df_corse` — almeno 80 righe:

- Colonne: `id_corsa`, `id_bici`, `id_utente`, `citta`, `data_corsa`, `durata_minuti`, `km_percorsi`, `fascia_oraria`
- Vincoli: almeno 3 date, 3 città (Milano / Roma / Torino), 5 duplicati, 8 NaN sparsi tra `durata_minuti` e `km_percorsi`

`df_bici` — almeno 20 righe:

- Colonne: `id_bici`, `tipo`, `citta`, `anno_acquisto`, `costo_acquisto`

`df_utenti` — almeno 25 righe:

- Colonne: `id_utente`, `nome`, `citta`, `tipo_abbonamento`, `data_iscrizione`

>**6.2 — Pulizia dati**

- Rimuovi le righe duplicate
- `durata_minuti` NaN → sostituisci con la mediana per città (usa `groupby` + `transform`)
- `km_percorsi` NaN → sostituisci con `durata_minuti * 0.18`
- Converti `data_corsa` da stringa a `datetime`
- Aggiungi colonne: `mese` (int) e `giorno_settimana` (es. `"Lunedì"`)
- Stampa `.info()` e `.describe()` prima e dopo la pulizia

>**6.3 — Apply e colonne derivate**

- Applica `classifica_corsa()` con `.apply()` → colonna `tipo_corsa`
- Calcola `velocita_media = km_percorsi / (durata_minuti / 60)`
- Calcola `costo_stimato` con `.apply()`:
  - Breve (< 15 min): € 1.50
  - Media (15–45 min): € 2.50 + € 0.10 × (minuti − 15)
  - Lunga (> 45 min): € 5.00 + € 0.08 × (minuti − 45)

>**6.4 — Aggregazioni e merge**

GroupBy :

- Per `citta`: numero corse, durata media, km totali, costo totale
- Per `fascia_oraria`: numero corse e velocità media
- Pivot table: indice = `citta`, colonne = `tipo_corsa`, valori = numero corse

Merge :

- Unisci `df_corse` + `df_bici` su `id_bici`, poi + `df_utenti` su `id_utente`
- Stampa le prime 5 righe e le colonne disponibili

Top-N :

- Le 5 biciclette con più corse
- I 3 utenti Premium con costo totale più alto
- *Aggiungi altre statistiche a piacere*

---

## Task 7 — Visualizzazione

> - Ogni grafico deve avere: titolo, etichette assi, legenda (dove necessaria).  
> - Aggiungi un commento nel codice (1-2 righe) con la domanda di business a cui risponde.
> - Deve essere salvato come png in una cartella apposita della repo

---

**Grafico 1 — Serie temporale corse**  → `output/01_serie_temporale.png`

- Matplotlib, line plot
- Una linea per città, colori distinti
- Usa `plt.rcParams` per almeno una personalizzazione globale

**Grafico 2 — Distribuzione durate per città**  → `output/02_distribuzione_durate.png`

- Seaborn `histplot` con KDE
- `hue` = città, tema `whitegrid`

**Grafico 3 — Corse per fascia oraria e tipo**  → `output/03_fasce_orarie.png`

- Seaborn `barplot`
- Barre raggruppate per tipo bicicletta (`classica` / `elettrica`)

**Grafico 4 — Scatter durata vs. velocità**  → `output/04_scatter_durata_velocita.png`

- Matplotlib scatter, colore punti per città
- Linea di tendenza con `np.polyfit`

**Grafico 5 — Dashboard riepilogativa**  → `output/05_dashboard.png`

- `plt.subplots(2, 2)` con `suptitle` e `tight_layout`
- In alto sx: bar chart corse per città
- In alto dx: pie chart abbonamenti utenti
- In basso sx: bar chart costo totale per città
- In basso dx: Seaborn `boxplot` durate per tipo corsa

>*Aggiungete altri grafici a vostra scelta*

---

## Consegna

- Crea un repository github e invia il link in chat

Il `README.md` deve contenere:

- Nome e cognome
- Descrizione del progetto (3-5 righe)
- Istruzioni: `pip install -r requirements.txt`
- Istruzioni per eseguire ogni script nell'ordine corretto
- Sezione *"Considerazioni"* (5-10 righe): cosa hai trovato difficile, cosa miglioreresti, un'osservazione sui dati

Il `requirements.txt` deve specificare le versioni:

```python
numpy>=1.24
pandas>=2.0
matplotlib>=3.7
seaborn>=0.12
```

> il repository deve essere **pubblico** al momento della consegna.  
> Non caricare `.pyc`, `__pycache__` o ambienti virtuali — usa `.gitignore`.

**il link alla repo la inviate a me all'email e99delsarto@gmail.com**

---

*Buona fortuna!*
