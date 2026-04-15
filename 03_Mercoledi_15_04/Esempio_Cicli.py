#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PANORAMICA COMPLETA SUI CICLI IN PYTHON
- for
- while
- range
- break, continue, pass
- cicli annidati
- iterazione su liste e dizionari
- enumerate e zip
"""

# ==============================================================
# 1. CICLO FOR BASE
# ==============================================================

print("=== FOR base ===")

for i in range(5):
    print(i)
print()


# ==============================================================
# 2. RANGE
# ==============================================================

print("=== RANGE ===")

print("range(5):")
for i in range(5):
    print(i)

print("range(2, 6):")
for i in range(2, 6):
    print(i)

print("range(0, 10, 2):")
for i in range(0, 10, 2):
    print(i)
print()


# ==============================================================
# 3. CICLO WHILE
# ==============================================================

print("=== WHILE ===")

n = 3
while n > 0:
    print(n)
    n -= 1
print("Fine ciclo")
print()


# ==============================================================
# 4. BREAK
# ==============================================================

print("=== BREAK ===")

for i in range(10):
    if i == 5:
        break
    print(i)
print()


# ==============================================================
# 5. CONTINUE
# ==============================================================

print("=== CONTINUE ===")

for i in range(5):
    if i == 2:
        continue
    print(i)
print()


# ==============================================================
# 6. PASS
# ==============================================================

print("=== PASS ===")

for i in range(3):
    if i == 1:
        pass  # non fa nulla
    print(i)
print()


# ==============================================================
# 7. CICLI SU LISTE
# ==============================================================

print("=== LISTE ===")

numeri = [10, 20, 30]

for n in numeri:
    print(n)
print()


# ==============================================================
# 8. CICLI SU STRINGHE
# ==============================================================

print("=== STRINGHE ===")

testo = "Python"

for c in testo:
    print(c)
print()


# ==============================================================
# 9. CICLI SU DIZIONARI
# ==============================================================

print("=== DIZIONARI ===")

persona = {"nome": "Anna", "eta": 25}

print("Chiavi:")
for k in persona:
    print(k)

print("Valori:")
for v in persona.values():
    print(v)

print("Chiave-valore:")
for k, v in persona.items():
    print(k, "->", v)
print()


# ==============================================================
# 10. ENUMERATE
# ==============================================================

print("=== ENUMERATE ===")

lista = ["a", "b", "c"]

for i, valore in enumerate(lista):
    print(i, valore)
print()


# ==============================================================
# 11. ZIP (più liste insieme)
# ==============================================================

print("=== ZIP ===")

nomi = ["Anna", "Luca", "Marco"]
eta = [25, 30, 35]

for n, e in zip(nomi, eta):
    print(n, e)
print()


# ==============================================================
# 12. CICLI ANNIDATI
# ==============================================================

print("=== CICLI ANNIDATI ===")

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
print()


# ==============================================================
# 13. LIST COMPREHENSION (ciclo compatto)
# ==============================================================

print("=== LIST COMPREHENSION ===")

quadrati = [x**2 for x in range(5)]
print("Quadrati:", quadrati)

pari = [x for x in range(10) if x % 2 == 0]
print("Pari:", pari)
print()


# ==============================================================
# 14. CICLO CON ELSE
# ==============================================================

print("=== FOR con ELSE ===")

for i in range(3):
    print(i)
else:
    print("Ciclo terminato senza break")
print()


# ==============================================================
# 15. ESEMPIO PRATICO: SOMMA NUMERI
# ==============================================================

print("=== ESEMPIO PRATICO ===")

numeri = [1, 2, 3, 4, 5]
somma = 0

for n in numeri:
    somma += n

print("Somma:", somma)
