#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PANORAMICA COMPLETA SUI MODULI IN PYTHON
- import base
- import con alias
- import selettivo
- moduli built-in
- creare un modulo
- __name__ == "__main__"
- sys.path
"""

# ==============================================================
# 1. IMPORT BASE
# ==============================================================

import math

print("=== 1. Import base ===")
print("Radice di 16:", math.sqrt(16))
print()


# ==============================================================
# 2. IMPORT CON ALIAS
# ==============================================================

import math as m

print("=== 2. Alias ===")
print("Pi greco:", m.pi)
print()


# ==============================================================
# 3. IMPORT SELETTIVO
# ==============================================================

from math import sqrt, pow

print("=== 3. Import selettivo ===")
print("sqrt(25):", sqrt(25))
print("pow(2, 3):", pow(2, 3))
print()


# ==============================================================
# 4. MODULI BUILT-IN
# ==============================================================

import random
import datetime

print("=== 4. Moduli built-in ===")
print("Numero casuale:", random.randint(1, 10))
print("Data attuale:", datetime.datetime.now())
print()


# ==============================================================
# 5. CREARE UN MODULO (ESEMPIO)
# ==============================================================

"""
Supponiamo di avere un file chiamato:

mio_modulo.py

contenuto:
-----------
def saluta(nome):
    return f"Ciao {nome}"

def somma(a, b):
    return a + b
-----------

Uso:
from mio_modulo import saluta, somma
"""

print("=== 5. Creazione modulo (teoria) ===")
print("Vedi commento nel codice")
print()


# ==============================================================
# 6. __name__ == "__main__"
# ==============================================================

print("=== 6. __name__ ===")

print("Nome del modulo corrente:", __name__)

def funzione_test():
    print("Questa funzione è eseguita")

if __name__ == "__main__":
    print("Eseguito direttamente")
    funzione_test()
print()


# ==============================================================
# 7. sys.path (dove Python cerca i moduli)
# ==============================================================

import sys

print("=== 7. sys.path ===")

for p in sys.path:
    print(p)
print()


# ==============================================================
# 8. IMPORT DI UN MODULO INTERO
# ==============================================================

import math

print("=== 8. Uso completo modulo ===")
print("Coseno:", math.cos(0))
print()


# ==============================================================
# 9. IMPORT TUTTO (sconsigliato)
# ==============================================================

from math import *

print("=== 9. Import * (sconsigliato) ===")
print("sqrt(36):", sqrt(36))
print()


# ==============================================================
# 10. RICARICARE UN MODULO (avanzato)
# ==============================================================

import importlib

print("=== 10. Reload modulo ===")

# esempio (solo se il modulo esiste):
# import mio_modulo
# importlib.reload(mio_modulo)

print("Reload spiegato nei commenti")
