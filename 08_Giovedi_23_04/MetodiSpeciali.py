### str e repr
from typing import Any


class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
    
    def __str__(self):
        return f"titolo: {self.titolo}, autore: {self.autore}"
    
    def __repr__(self):
        return f"Libro(titolo[self]: {self.titolo} - autore[self]: {self.autore})"
    
# l1 = Libro("Boccata D'aria", "George Orwell")

# print(l1)
# print(repr(l1))

### len
class Squadra:
    def __init__(self, giocatori: list[str]):
        self.giocatori = giocatori
    
    def __len__(self):
        return len(self.giocatori)
    
# squ = Squadra(["Pippo", "Caio", "Mirko"])
# print(len(squ))

#equals
class Prodotto:
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo
    
    def __eq__(self, altro):
        if not isinstance(altro, Prodotto):
            return False
        
        return self.nome == altro.nome and self.prezzo == altro.prezzo 

# p1 = Prodotto("Tablet", 120)
# p2 = Prodotto("Tablet", 130)

# print(p1==p2)

#get attribute

class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def __getattribute__(self, attributo):
        print(f"sto accedendo all'attributo {attributo}")
        return super().__getattribute__(attributo)
    
p = Persona("Marta", 23)

print(p.nome)
print(p.eta)