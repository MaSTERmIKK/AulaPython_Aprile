#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DIZIONARI + MATRICI IN PYTHON

- Dizionari base
- Dizionari annidati
- Dizionari con matrici (liste di liste)
- Matrici base (liste)
- Operazioni su matrici
- Matrici con NumPy
- Dizionari + NumPy (caso reale)
"""

import numpy as np


# ==============================================================
# 1. DIZIONARI BASE
# ==============================================================

print("=== 1. Dizionari base ===")

persona = {
    "nome": "Anna",
    "eta": 25,
    "citta": "Roma"
}

print(persona)
print("Nome:", persona["nome"])
print()


# ==============================================================
# 2. DIZIONARI ANNIDATI
# ==============================================================

print("=== 2. Dizionari annidati ===")

studenti = {
    "s1": {"nome": "Luca", "voto": 28},
    "s2": {"nome": "Marco", "voto": 30}
}

for k, v in studenti.items():
    print(k, v["nome"], v["voto"])
print()


# ==============================================================
# 3. MATRICE BASE (LISTA DI LISTE)
# ==============================================================

print("=== 3. Matrice base ===")

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Elemento [1][2]:", matrice[1][2])

for riga in matrice:
    print(riga)
print()


# ==============================================================
# 4. SOMMA DI DUE MATRICI (liste)
# ==============================================================

print("=== 4. Somma matrici ===")

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

C = []

for i in range(len(A)):
    riga = []
    for j in range(len(A[0])):
        riga.append(A[i][j] + B[i][j])
    C.append(riga)

print("Risultato:", C)
print()


# ==============================================================
# 5. DIZIONARIO CON MATRICE
# ==============================================================

print("=== 5. Dizionario con matrice ===")

dati = {
    "nome": "Classe A",
    "voti": [
        [6, 7, 8],
        [5, 6, 7],
        [9, 8, 7]
    ]
}

print("Voti:")
for riga in dati["voti"]:
    print(riga)
print()


# ==============================================================
# 6. MEDIA PER RIGA (MATRICE)
# ==============================================================

print("=== 6. Media per riga ===")

for riga in dati["voti"]:
    media = sum(riga) / len(riga)
    print("Media:", media)
print()


# ==============================================================
# 7. MATRICE CON NUMPY
# ==============================================================

print("=== 7. NumPy ===")

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("A:\n", A)
print("B:\n", B)

print("Somma:\n", A + B)
print("Moltiplicazione elemento:\n", A * B)
print("Prodotto matriciale:\n", A @ B)
print()


# ==============================================================
# 8. DIZIONARIO + NUMPY
# ==============================================================

print("=== 8. Dizionario + NumPy ===")

dataset = {
    "nome": "Vendite",
    "dati": np.array([
        [10, 20, 30],
        [5, 15, 25],
        [8, 18, 28]
    ])
}

print("Dati:\n", dataset["dati"])

print("Somma totale:", dataset["dati"].sum())
print("Media per colonna:", dataset["dati"].mean(axis=0))
print()


# ==============================================================
# 9. ACCESSO AVANZATO
# ==============================================================

print("=== 9. Accesso avanzato ===")

print("Elemento [0,1]:", dataset["dati"][0, 1])
print("Prima riga:", dataset["dati"][0])
print("Prima colonna:", dataset["dati"][:, 0])
print()


# ==============================================================
# 10. CASO PRATICO: SOMMA PER STUDENTE
# ==============================================================

print("=== 10. Caso pratico ===")

registro = {
    "Anna": [7, 8, 9],
    "Luca": [6, 7, 6],
    "Marco": [9, 9, 8]
}

for nome, voti in registro.items():
    totale = sum(voti)
    media = totale / len(voti)
    print(nome, "- Totale:", totale, "- Media:", media)
