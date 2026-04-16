#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PANORAMICA COMPLETA SULLE FUNZIONI IN PYTHON
- definizione
- parametri
- return
- default arguments
- *args e **kwargs
- lambda
- funzioni annidate
- scope
- ricorsione
"""

# ==============================================================
# 1. FUNZIONE BASE
# ==============================================================

def saluta():
    print("Ciao!")

saluta()
print()


# ==============================================================
# 2. FUNZIONE CON PARAMETRI
# ==============================================================

def saluta_nome(nome):
    print("Ciao", nome)

saluta_nome("Mario")
saluta_nome("Anna")
print()


# ==============================================================
# 3. FUNZIONE CON RETURN
# ==============================================================

def somma(a, b):
    return a + b

risultato = somma(5, 3)
print("Somma:", risultato)
print()


# ==============================================================
# 4. PARAMETRI DEFAULT
# ==============================================================

def potenza(base, esponente=2):
    return base ** esponente

print("Quadrato:", potenza(4))
print("Cubo:", potenza(4, 3))
print()


# ==============================================================
# 5. *args (numero variabile di argomenti)
# ==============================================================

def somma_tutti(*numeri):
    totale = 0
    for n in numeri:
        totale += n
    return totale

print("Somma variabile:", somma_tutti(1, 2, 3, 4))
print()


# ==============================================================
# 6. **kwargs (parametri con nome)
# ==============================================================

def stampa_dati(**dati):
    for chiave, valore in dati.items():
        print(chiave, ":", valore)

stampa_dati(nome="Luca", eta=30, citta="Roma")
print()


# ==============================================================
# 7. FUNZIONI LAMBDA
# ==============================================================

quadrato = lambda x: x ** 2

print("Lambda quadrato:", quadrato(5))

somma = lambda a, b: a + b
print("Lambda somma:", somma(2, 3))
print()


# ==============================================================
# 8. FUNZIONI ANNIDATE
# ==============================================================

def esterna(x):
    def interna(y):
        return y * 2
    return interna(x)

print("Funzione annidata:", esterna(5))
print()


# ==============================================================
# 9. SCOPE (locale/globale)
# ==============================================================

x = 10  # globale

def modifica():
    x = 5  # locale
    print("Dentro funzione:", x)

modifica()
print("Fuori funzione:", x)
print()


# ==============================================================
# 10. USO DI GLOBAL
# ==============================================================

contatore = 0

def incrementa():
    global contatore
    contatore += 1

incrementa()
incrementa()
print("Contatore globale:", contatore)
print()


# ==============================================================
# 11. RITORNO MULTIPLO
# ==============================================================

def operazioni(a, b):
    return a + b, a - b, a * b

s, d, m = operazioni(6, 2)
print("Somma:", s, "Diff:", d, "Prod:", m)
print()


# ==============================================================
# 12. FUNZIONI COME PARAMETRI
# ==============================================================

def applica_funzione(f, valore):
    return f(valore)

def triplo(x):
    return x * 3

print("Applica funzione:", applica_funzione(triplo, 4))
print()


# ==============================================================
# 13. RICORSIONE
# ==============================================================

def fattoriale(n):
    if n == 0:
        return 1
    return n * fattoriale(n - 1)

print("Fattoriale 5:", fattoriale(5))
print()


# ==============================================================
# 14. FUNZIONE CON CONDIZIONI
# ==============================================================

def pari_o_dispari(n):
    return "Pari" if n % 2 == 0 else "Dispari"

print("7 è:", pari_o_dispari(7))
print()


# ==============================================================
# 15. FUNZIONE CON LISTE
# ==============================================================

def filtra_pari(lista):
    return [x for x in lista if x % 2 == 0]

print("Pari:", filtra_pari([1, 2, 3, 4, 5, 6]))
