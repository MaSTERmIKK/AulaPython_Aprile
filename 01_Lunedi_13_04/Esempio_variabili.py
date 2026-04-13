#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PANORAMICA COMPLETA SULLE VARIABILI IN PYTHON
- Tipi base
- Assegnazione
- Dinamicità
- Operazioni
- Casting
- Naming
- Scope
"""

# ==============================================================
# 1. ASSEGNAZIONE DI VARIABILI
# ==============================================================

x = 10
nome = "Mario"
pi = 3.14
attivo = True

print("x =", x)
print("nome =", nome)
print("pi =", pi)
print("attivo =", attivo)
print()


# ==============================================================
# 2. TIPI DI DATI
# ==============================================================

print("=== Tipi ===")
print(type(x))        # int
print(type(nome))     # str
print(type(pi))       # float
print(type(attivo))   # bool
print()


# ==============================================================
# 3. ASSEGNAZIONE MULTIPLA
# ==============================================================

a, b, c = 1, 2, 3
print("a, b, c =", a, b, c)

# stesso valore a più variabili
x = y = z = 100
print("x, y, z =", x, y, z)
print()


# ==============================================================
# 4. VARIABILI DINAMICHE
# ==============================================================

var = 10
print("var:", var, type(var))

var = "Ora sono una stringa"
print("var:", var, type(var))
print()


# ==============================================================
# 5. OPERAZIONI SU VARIABILI
# ==============================================================

a = 10
b = 3

print("Somma:", a + b)
print("Differenza:", a - b)
print("Moltiplicazione:", a * b)
print("Divisione:", a / b)
print("Divisione intera:", a // b)
print("Modulo:", a % b)
print("Potenza:", a ** b)
print()


# ==============================================================
# 6. CASTING (conversione tipi)
# ==============================================================

numero = "123"

print("Stringa:", numero, type(numero))

numero_int = int(numero)
print("Convertito in int:", numero_int, type(numero_int))

numero_float = float(numero)
print("Convertito in float:", numero_float, type(numero_float))
print()


# ==============================================================
# 7. STRINGHE E VARIABILI
# ==============================================================

nome = "Anna"
eta = 25

print("Ciao", nome, "hai", eta, "anni")

# f-string (modo moderno)
print(f"Ciao {nome}, hai {eta} anni")
print()


# ==============================================================
# 8. COSTANTI (convenzione)
# ==============================================================

PI_GRECO = 3.14159
MAX_UTENTI = 100

print("Costanti:", PI_GRECO, MAX_UTENTI)
print()


# ==============================================================
# 9. NAMING DELLE VARIABILI
# ==============================================================

# valido
numero_studenti = 25

# non valido (commentato)
# 2numero = 10
# nome-cognome = "x"

print("numero_studenti =", numero_studenti)
print()


# ==============================================================
# 10. VARIABILI GLOBALI E LOCALI
# ==============================================================

x = 50  # globale

def esempio_scope():
    x = 10  # locale
    print("Dentro funzione:", x)

esempio_scope()
print("Fuori funzione:", x)
print()


# ==============================================================
# 11. USO DI GLOBAL
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
# 12. SWAP DI VARIABILI
# ==============================================================

a = 5
b = 10

print("Prima:", a, b)

a, b = b, a

print("Dopo:", a, b)
