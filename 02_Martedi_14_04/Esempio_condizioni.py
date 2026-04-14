#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PANORAMICA SU CONDIZIONI E MATCH IN PYTHON
- if, elif, else
- operatori logici
- confronti
- condizioni annidate
- operatore ternario
- match-case (pattern matching)
"""

# ==============================================================
# 1. IF BASE
# ==============================================================

x = 10

if x > 5:
    print("x è maggiore di 5")
print()


# ==============================================================
# 2. IF - ELSE
# ==============================================================

numero = 4

if numero % 2 == 0:
    print("Numero pari")
else:
    print("Numero dispari")
print()


# ==============================================================
# 3. IF - ELIF - ELSE
# ==============================================================

voto = 27

if voto >= 28:
    print("Ottimo")
elif voto >= 24:
    print("Buono")
elif voto >= 18:
    print("Sufficiente")
else:
    print("Insufficiente")
print()


# ==============================================================
# 4. OPERATORI LOGICI
# ==============================================================

eta = 20
studente = True

if eta > 18 and studente:
    print("Studente maggiorenne")

if eta < 18 or studente:
    print("Minorenne o studente")

if not studente:
    print("Non è uno studente")
print()


# ==============================================================
# 5. CONDIZIONI ANNIDATE
# ==============================================================

numero = 15

if numero > 0:
    if numero % 3 == 0:
        print("Positivo e multiplo di 3")
print()


# ==============================================================
# 6. OPERATORE TERNARIO
# ==============================================================

x = 7
risultato = "Pari" if x % 2 == 0 else "Dispari"

print("Numero:", x, "-", risultato)
print()


# ==============================================================
# 7. MATCH-CASE (switch moderno)
# ==============================================================

giorno = 3

match giorno:
    case 1:
        print("Lunedì")
    case 2:
        print("Martedì")
    case 3:
        print("Mercoledì")
    case _:
        print("Altro giorno")
print()


# ==============================================================
# 8. MATCH CON PIÙ VALORI
# ==============================================================

voto = 30

match voto:
    case 30 | 31:
        print("Eccellente")
    case 28 | 29:
        print("Ottimo")
    case _:
        print("Altro voto")
print()


# ==============================================================
# 9. MATCH CON VARIABILI
# ==============================================================

comando = "start"

match comando:
    case "start":
        print("Avvio sistema")
    case "stop":
        print("Arresto sistema")
    case _:
        print("Comando sconosciuto")
print()


# ==============================================================
# 10. MATCH CON CONDIZIONE (GUARD)
# ==============================================================

numero = 15

match numero:
    case n if n % 2 == 0:
        print("Numero pari")
    case n if n % 2 != 0:
        print("Numero dispari")
print()


# ==============================================================
# 11. MATCH CON TUPLE
# ==============================================================

punto = (0, 5)

match punto:
    case (0, 0):
        print("Origine")
    case (0, y):
        print("Asse Y, valore:", y)
    case (x, 0):
        print("Asse X, valore:", x)
    case _:
        print("Altro punto")
print()


# ==============================================================
# 12. MATCH CON DIZIONARI
# ==============================================================

utente = {"nome": "Anna", "eta": 25}

match utente:
    case {"nome": nome, "eta": eta}:
        print(f"Utente: {nome}, età {eta}")
    case _:
        print("Struttura sconosciuta")
