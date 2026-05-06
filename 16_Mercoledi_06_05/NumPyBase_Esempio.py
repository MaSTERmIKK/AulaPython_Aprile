#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
NUMPY - ESEMPI BASE

Contenuti:
1) Creazione array
2) Shape e dimensioni
3) Indicizzazione e slicing
4) Operazioni matematiche
5) Funzioni utili
6) Matrici
7) Broadcasting base
8) Random
"""

import numpy as np


# ==============================================================
# 1. CREAZIONE ARRAY
# ==============================================================

print("=== 1. Creazione Array ===")

a = np.array([1, 2, 3, 4])
print("Array:", a)

b = np.array([[1, 2], [3, 4]])
print("Matrice:\n", b)

zeri = np.zeros((2, 3))
print("Zeri:\n", zeri)

uno = np.ones((2, 2))
print("Uno:\n", uno)

range_array = np.arange(0, 10, 2)
print("Arange:", range_array)

lin = np.linspace(0, 1, 5)
print("Linspace:", lin)
print()


# ==============================================================
# 2. SHAPE E DIMENSIONI
# ==============================================================

print("=== 2. Shape ===")

m = np.array([[1, 2, 3],
              [4, 5, 6]])

print("Shape:", m.shape)
print("Dimensioni:", m.ndim)
print("Numero elementi:", m.size)
print()


# ==============================================================
# 3. INDICIZZAZIONE E SLICING
# ==============================================================

print("=== 3. Indicizzazione ===")

x = np.array([10, 20, 30, 40, 50])

print("Elemento indice 2:", x[2])
print("Slice 1:4:", x[1:4])

mat = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Elemento [1,2]:", mat[1, 2])
print("Prima riga:", mat[0])
print("Prima colonna:", mat[:, 0])
print()


# ==============================================================
# 4. OPERAZIONI MATEMATICHE
# ==============================================================

print("=== 4. Operazioni ===")

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print("Somma:", a + b)
print("Moltiplicazione:", a * b)
print("Potenza:", a ** 2)
print("Radice:", np.sqrt(a))
print()


# ==============================================================
# 5. FUNZIONI UTILI
# ==============================================================

print("=== 5. Funzioni utili ===")

v = np.array([1, 2, 3, 4, 5])

print("Somma:", np.sum(v))
print("Media:", np.mean(v))
print("Massimo:", np.max(v))
print("Minimo:", np.min(v))
print("Deviazione standard:", np.std(v))
print()


# ==============================================================
# 6. MATRICI
# ==============================================================

print("=== 6. Matrici ===")

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Somma matrici:\n", A + B)

print("Moltiplicazione elemento:\n", A * B)

print("Prodotto matriciale:\n", A @ B)

print("Trasposta:\n", A.T)
print()


# ==============================================================
# 7. BROADCASTING BASE
# ==============================================================

print("=== 7. Broadcasting ===")

mat = np.array([[1, 2, 3],
                [4, 5, 6]])

vettore = np.array([10, 20, 30])

print("Matrice:\n", mat)
print("Vettore:", vettore)

print("Risultato:\n", mat + vettore)
print()


# ==============================================================
# 8. RANDOM
# ==============================================================

print("=== 8. Random ===")

np.random.seed(42)

print("Random uniformi:\n", np.random.rand(2, 3))

print("Random interi:\n", np.random.randint(0, 10, 5))

print("Random normali:\n", np.random.randn(3))
