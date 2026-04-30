#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PANORAMICA COMPLETA SU I/O FILE (TXT + CSV)
- Scrittura file txt
- Lettura file txt
- Modalità file (r, w, a)
- Gestione file con with
- Scrittura CSV
- Lettura CSV
- Uso del modulo csv
"""

import csv


# ==============================================================
# 1. SCRITTURA FILE TXT
# ==============================================================

print("=== 1. Scrittura TXT ===")

with open("file.txt", "w", encoding="utf-8") as f:
    f.write("Prima riga\n")
    f.write("Seconda riga\n")

print("File TXT scritto\n")


# ==============================================================
# 2. LETTURA FILE TXT
# ==============================================================

print("=== 2. Lettura TXT ===")

with open("file.txt", "r", encoding="utf-8") as f:
    contenuto = f.read()
    print(contenuto)


# ==============================================================
# 3. LETTURA RIGA PER RIGA
# ==============================================================

print("=== 3. Lettura riga per riga ===")

with open("file.txt", "r", encoding="utf-8") as f:
    for riga in f:
        print(riga.strip())
print()


# ==============================================================
# 4. APPEND (AGGIUNTA)
# ==============================================================

print("=== 4. Append ===")

with open("file.txt", "a", encoding="utf-8") as f:
    f.write("Nuova riga aggiunta\n")

print("Riga aggiunta\n")


# ==============================================================
# 5. SCRITTURA CSV
# ==============================================================

print("=== 5. Scrittura CSV ===")

dati = [
    ["nome", "eta", "citta"],
    ["Anna", 25, "Roma"],
    ["Luca", 30, "Milano"],
    ["Marco", 35, "Napoli"]
]

with open("file.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(dati)

print("CSV scritto\n")


# ==============================================================
# 6. LETTURA CSV
# ==============================================================

print("=== 6. Lettura CSV ===")

with open("file.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for riga in reader:
        print(riga)
print()


# ==============================================================
# 7. CSV COME DIZIONARI
# ==============================================================

print("=== 7. CSV DictReader ===")

with open("file.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for riga in reader:
        print(riga["nome"], "-", riga["eta"])
print()


# ==============================================================
# 8. SCRITTURA CSV CON DIZIONARI
# ==============================================================

print("=== 8. CSV DictWriter ===")

campi = ["nome", "eta", "citta"]

persone = [
    {"nome": "Sara", "eta": 28, "citta": "Torino"},
    {"nome": "Giulia", "eta": 32, "citta": "Bologna"}
]

with open("file_dict.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=campi)
    writer.writeheader()
    writer.writerows(persone)

print("CSV con dizionari scritto\n")


# ==============================================================
# 9. LETTURA SICURA CON TRY/EXCEPT
# ==============================================================

print("=== 9. Gestione errori ===")

try:
    with open("inesistente.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File non trovato")
