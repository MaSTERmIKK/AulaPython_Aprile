#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PANORAMICA COMPLETA SUL POLIMORFISMO IN PYTHON

- Polimorfismo tramite ereditarietà (override)
- Duck typing
- Funzioni polimorfiche
- Operator overloading
- Polimorfismo built-in
"""

# ==============================================================
# 1. POLIMORFISMO CON EREDITARIETÀ (OVERRIDING)
# ==============================================================

class Animale:
    def verso(self):
        return "Verso generico"

class Cane(Animale):
    def verso(self):
        return "Bau!"

class Gatto(Animale):
    def verso(self):
        return "Miao!"

print("=== 1. Override ===")
animali = [Cane(), Gatto(), Animale()]

for a in animali:
    print(a.verso())
print()


# ==============================================================
# 2. FUNZIONE POLIMORFICA
# ==============================================================

def fai_parlare(animale):
    print(animale.verso())

print("=== 2. Funzione polimorfica ===")
fai_parlare(Cane())
fai_parlare(Gatto())
print()


# ==============================================================
# 3. DUCK TYPING
# ==============================================================

class Auto:
    def muovi(self):
        return "L'auto corre"

class Barca:
    def muovi(self):
        return "La barca naviga"

class Aereo:
    def muovi(self):
        return "L'aereo vola"

def fai_muovere(oggetto):
    print(oggetto.muovi())

print("=== 3. Duck Typing ===")
mezzi = [Auto(), Barca(), Aereo()]

for m in mezzi:
    fai_muovere(m)
print()


# ==============================================================
# 4. OPERATOR OVERLOADING
# ==============================================================

class Vettore:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, altro):
        return Vettore(self.x + altro.x, self.y + altro.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

print("=== 4. Operator Overloading ===")
v1 = Vettore(1, 2)
v2 = Vettore(3, 4)

v3 = v1 + v2
print("Somma vettori:", v3)
print()


# ==============================================================
# 5. POLIMORFISMO BUILT-IN
# ==============================================================

print("=== 5. Built-in polymorphism ===")

print("len string:", len("ciao"))
print("len lista:", len([1, 2, 3]))
print("len dict:", len({"a": 1, "b": 2}))
print()


# ==============================================================
# 6. METODI CON STESSO NOME (comportamento diverso)
# ==============================================================

class Rettangolo:
    def area(self):
        return 10 * 5

class Cerchio:
    def area(self):
        return 3.14 * 3 * 3

print("=== 6. Metodo comune ===")
forme = [Rettangolo(), Cerchio()]

for f in forme:
    print("Area:", f.area())
print()


# ==============================================================
# 7. POLIMORFISMO CON COLLEZIONI
# ==============================================================

print("=== 7. Collezioni polimorfiche ===")

oggetti = [Cane(), Gatto(), Auto(), Barca()]

for obj in oggetti:
    # controllo dinamico del metodo disponibile
    if hasattr(obj, "verso"):
        print(obj.verso())
    elif hasattr(obj, "muovi"):
        print(obj.muovi())
print()


# ==============================================================
# 8. POLIMORFISMO CON FUNZIONI DIVERSE (stesso nome logico)
# ==============================================================

def somma(a, b):
    return a + b

print("=== 8. Funzione polimorfica (tipi diversi) ===")

print(somma(2, 3))             # int
print(somma("Ciao ", "Mondo")) # stringhe
print(somma([1, 2], [3, 4]))   # liste
print()


# ==============================================================
# 9. POLIMORFISMO AVANZATO: ITERABILI
# ==============================================================

def stampa_tutti(iterabile):
    for elemento in iterabile:
        print(elemento)

print("=== 9. Iterabili ===")

stampa_tutti([1, 2, 3])
stampa_tutti("ABC")
stampa_tutti((10, 20))
