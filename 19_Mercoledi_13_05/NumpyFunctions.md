# Funzioni NumPy: Aritmetiche, Matematiche, Statistiche e Matriciali

---

## Operazioni Aritmetiche

### `np.add(a, b)`

**Esempio pratico**

```python
np.add([10, 20], [1, 2])  # → [11, 22]
```

**Spiegazione teorica**
Somma due array elemento per elemento. Equivalente all'operatore `+`.

**Esempio di utilizzo**
Combinare i ricavi mensili di due negozi per ottenere il totale complessivo.

---

### `np.subtract(a, b)`

**Esempio pratico**

```python
np.subtract([10, 20], [1, 2])  # → [9, 18]
```

**Spiegazione teorica**
Sottrae il secondo array dal primo, elemento per elemento. Equivalente all'operatore `-`.

**Esempio di utilizzo**
Calcolare la differenza tra le temperature massime e minime di ogni giorno della settimana.

---

### `np.multiply(a, b)`

**Esempio pratico**

```python
np.multiply([10, 20], [1, 2])  # → [10, 40]
```

**Spiegazione teorica**
Moltiplica due array elemento per elemento. Equivalente all'operatore `*`. **Non** è il prodotto matriciale.

**Esempio di utilizzo**
Calcolare il costo totale moltiplicando la quantità di ogni prodotto per il suo prezzo unitario.

---

### `np.divide(a, b)`

**Esempio pratico**

```python
np.divide([10, 20], [2, 4])  # → [5.0, 5.0]
```

**Spiegazione teorica**
Divide il primo array per il secondo, elemento per elemento. Il risultato è sempre in virgola mobile.

**Esempio di utilizzo**
Normalizzare i punteggi di studenti dividendo ciascun voto per il massimo ottenibile.

---

## Funzioni Matematiche

### `np.sin(x)`

**Esempio pratico**

```python
np.sin([0, np.pi / 2])  # → [0.0, 1.0]
```

**Spiegazione teorica**
Calcola il seno di ogni elemento dell'array. I valori devono essere espressi in **radianti**.

**Esempio di utilizzo**
Modellare un'onda sonora o un segnale oscillante nel tempo.

---

### `np.cos(x)`

**Esempio pratico**

```python
np.cos([0, np.pi])  # → [1.0, -1.0]
```

**Spiegazione teorica**
Calcola il coseno di ogni elemento dell'array, in radianti. Descrive la componente orizzontale di un vettore rotante.

**Esempio di utilizzo**
Calcolare le coordinate x di punti disposti su una circonferenza, dato l'angolo di ciascuno.

---

### `np.exp(x)`

**Esempio pratico**

```python
np.exp([0, 1, 2])  # → [1.0, 2.718, 7.389]
```

**Spiegazione teorica**
Calcola $e^x$ per ogni elemento, dove $e \approx 2.718$. Modella fenomeni con crescita o decrescita proporzionale al valore corrente.

**Esempio di utilizzo**
Simulare la crescita di una popolazione batterica nel tempo.

---

### `np.log(x)`

**Esempio pratico**

```python
np.log([1, np.e, np.e**2])  # → [0.0, 1.0, 2.0]
```

**Spiegazione teorica**
Calcola il logaritmo naturale (base $e$) di ogni elemento. È l'inverso di `np.exp`.

**Esempio di utilizzo**
Comprimere una scala di valori molto ampia (es. magnitudine di terremoti o intensità sonora in decibel).

---

## Statistica

### `np.mean(x)`

**Esempio pratico**

```python
np.mean([2, 4, 6, 8, 10])  # → 6.0
```

**Spiegazione teorica**
Calcola la media aritmetica: somma tutti i valori e divide per il numero di elementi.

**Esempio di utilizzo**
Calcolare il voto medio di uno studente durante il semestre.

---

### `np.median(x)`

**Esempio pratico**

```python
np.median([1, 2, 100])  # → 2.0
```

**Spiegazione teorica**
Restituisce il valore centrale dell'array ordinato. È meno sensibile ai valori estremi (outlier) rispetto alla media.

**Esempio di utilizzo**
Determinare il reddito "tipico" in una popolazione, dove pochi stipendi altissimi non distorcono il risultato.

---

### `np.std(x)`

**Esempio pratico**

```python
np.std([2, 4, 6, 8, 10])  # → 2.828
```

**Spiegazione teorica**
Calcola la deviazione standard, ovvero quanto i valori si discostano in media dal valore medio.

**Esempio di utilizzo**
Valutare la costanza delle prestazioni di un atleta: una deviazione bassa indica risultati stabili.

---

### `np.var(x)`

**Esempio pratico**

```python
np.var([2, 4, 6, 8, 10])  # → 8.0
```

**Spiegazione teorica**
Calcola la varianza, ovvero il quadrato della deviazione standard. Misura la dispersione complessiva dei dati.

**Esempio di utilizzo**
Confrontare la variabilità dei prezzi di due titoli azionari per valutare il rischio di investimento.

---

## Trasformate e Analisi dei Segnali

### `np.fft.fft(x)`

**Esempio pratico**

```python
np.fft.fft([1, 0, 1, 0])
# → [2.+0.j, 0.+0.j, 2.+0.j, 0.+0.j]
```

**Spiegazione teorica**
Calcola la Trasformata Discreta di Fourier (DFT) di un segnale, convertendolo dal dominio del tempo al dominio delle frequenze.

**Esempio di utilizzo**
Identificare le frequenze dominanti in un segnale audio o in una serie temporale di sensori.

---

## Prodotto Matriciale e Algebra Lineare

### `np.dot(A, B)`

**Esempio pratico**

```python
np.dot([[1, 2], [3, 4]], [[5, 6], [7, 8]])
# → [[19, 22], [43, 50]]
```

**Spiegazione teorica**
Esegue il prodotto matriciale tra due matrici (o scalare tra due vettori). Ogni elemento del risultato è la somma dei prodotti riga × colonna.

**Esempio di utilizzo**
Applicare una trasformazione lineare (rotazione, scala) a un insieme di punti 2D.

---

### `np.matmul(A, B)`

**Esempio pratico**

```python
np.matmul([[1, 2], [3, 4]], [[5, 6], [7, 8]])
# → [[19, 22], [43, 50]]
```

**Spiegazione teorica**
Esegue il prodotto matriciale come `np.dot`, ma è la funzione preferita per le matrici. Non supporta la moltiplicazione con scalari.

**Esempio di utilizzo**
Calcolare la propagazione in avanti (forward pass) di uno strato di una rete neurale.

---

### `np.linalg.det(A)`

**Esempio pratico**

```python
np.linalg.det([[1, 2], [3, 4]])  # → -2.0
```

**Spiegazione teorica**
Calcola il determinante di una matrice quadrata. Se il determinante è zero, la matrice non è invertibile.

**Esempio di utilizzo**
Verificare se un sistema di equazioni lineari ha una soluzione unica prima di risolverlo.

---

### `np.linalg.inv(A)`

**Esempio pratico**

```python
np.linalg.inv([[1, 2], [3, 4]])
# → [[-2.0, 1.0], [1.5, -0.5]]
```

**Spiegazione teorica**
Calcola la matrice inversa $A^{-1}$ tale che $A \cdot A^{-1} = I$ (matrice identità). Esiste solo se il determinante è diverso da zero.

**Esempio di utilizzo**
Risolvere un sistema lineare $Ax = b$ calcolando $x = A^{-1}b$.

---

### `np.linalg.eig(A)`

**Esempio pratico**

```python
valori, vettori = np.linalg.eig([[1, 2], [3, 4]])
# valori → [-0.372, 5.372]
```

**Spiegazione teorica**
Restituisce autovalori e autovettori di una matrice quadrata. Un autovettore $v$ soddisfa $Av = \lambda v$, dove $\lambda$ è l'autovalore corrispondente.

**Esempio di utilizzo**
Applicare la PCA (Principal Component Analysis) per ridurre la dimensionalità di un dataset.

---

### `np.linalg.norm(x)`

**Esempio pratico**

```python
np.linalg.norm([3, 4])  # → 5.0
```

**Spiegazione teorica**
Calcola la norma di un vettore o di una matrice. Di default usa la norma euclidea ($L_2$) per i vettori.

**Esempio di utilizzo**
Misurare la lunghezza di un vettore spostamento o la distanza tra due punti nello spazio.

---

### `np.linalg.solve(A, b)`

**Esempio pratico**

```python
np.linalg.solve([[1, 2], [3, 4]], [5, 11])
# → [1.0, 2.0]
```

**Spiegazione teorica**
Risolve il sistema lineare $Ax = b$ trovando il vettore $x$. È più stabile numericamente rispetto a calcolare $A^{-1}b$ esplicitamente.

**Esempio di utilizzo**
Trovare le quantità di due prodotti da mescolare per rispettare vincoli di peso e costo in un problema di ottimizzazione.
