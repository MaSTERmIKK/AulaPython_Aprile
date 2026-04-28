#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PANORAMICA COMPLETA SULL'ASTRAZIONE IN PYTHON

- Classi astratte (ABC)
- Metodi astratti
- Metodi concreti nelle classi astratte
- Interfacce astratte
- Proprietà astratte
- Template Method Pattern
- Polimorfismo basato su astrazione
"""

from abc import ABC, abstractmethod


# ==============================================================
# 1. CLASSE ASTRATTA BASE
# ==============================================================

class Animale(ABC):

    @abstractmethod
    def verso(self):
        pass

    def descrizione(self):
        return "Sono un animale"


class Cane(Animale):
    def verso(self):
        return "Bau!"


class Gatto(Animale):
    def verso(self):
        return "Miao!"


print("=== 1. Classe Astratta ===")
animali = [Cane(), Gatto()]

for a in animali:
    print(a.descrizione(), "-", a.verso())
print()


# ==============================================================
# 2. INTERFACCIA ASTRATTA (solo metodi astratti)
# ==============================================================

class Forma(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Rettangolo(Forma):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def area(self):
        return self.base * self.altezza

    def perimetro(self):
        return 2 * (self.base + self.altezza)


class Cerchio(Forma):
    def __init__(self, raggio):
        self.raggio = raggio

    def area(self):
        return 3.14 * self.raggio ** 2

    def perimetro(self):
        return 2 * 3.14 * self.raggio


print("=== 2. Interfaccia Forma ===")
forme = [Rettangolo(4, 5), Cerchio(3)]

for f in forme:
    print("Area:", f.area(), "Perimetro:", f.perimetro())
print()


# ==============================================================
# 3. PROPRIETÀ ASTRATTA
# ==============================================================

class Veicolo(ABC):

    @property
    @abstractmethod
    def tipo(self):
        pass

    @abstractmethod
    def muovi(self):
        pass


class Auto(Veicolo):
    @property
    def tipo(self):
        return "Auto"

    def muovi(self):
        return "Si muove su strada"


class Barca(Veicolo):
    @property
    def tipo(self):
        return "Barca"

    def muovi(self):
        return "Si muove in acqua"


print("=== 3. Proprietà astratta ===")
mezzi = [Auto(), Barca()]

for m in mezzi:
    print(m.tipo, "-", m.muovi())
print()


# ==============================================================
# 4. TEMPLATE METHOD PATTERN
# ==============================================================

class Processo(ABC):

    def esegui(self):
        print("Start processo")
        self.step1()
        self.step2()
        print("Fine processo")

    @abstractmethod
    def step1(self):
        pass

    @abstractmethod
    def step2(self):
        pass


class ProcessoPagamento(Processo):
    def step1(self):
        print("Controllo fondi")

    def step2(self):
        print("Pagamento eseguito")


class ProcessoRegistrazione(Processo):
    def step1(self):
        print("Validazione dati")

    def step2(self):
        print("Utente registrato")


print("=== 4. Template Method ===")
ProcessoPagamento().esegui()
print()
ProcessoRegistrazione().esegui()
print()


# ==============================================================
# 5. POLIMORFISMO TRAMITE ASTRAZIONE
# ==============================================================

def esegui_movimento(oggetto):
    print(oggetto.muovi())


print("=== 5. Polimorfismo con astrazione ===")
esegui_movimento(Auto())
esegui_movimento(Barca())
print()


# ==============================================================
# 6. ERRORE: ISTANZIAZIONE DIRETTA
# ==============================================================

print("=== 6. Tentativo di istanziare classe astratta ===")

try:
    a = Animale()
except TypeError as e:
    print("Errore:", e)
