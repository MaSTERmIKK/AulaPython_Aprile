class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
    
    def mostra_info(self):
        print(f"Veicolo marca {self.marca}, modello {self.modello}")

class DotazioniSpeciali:
    def __init__(self, dotazioni: list[str]):
        self.dotazioni = dotazioni
    
    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")

class AutoSportiva(Veicolo, DotazioniSpeciali):

    def __init__(self, marca, modello, dotazioni, cavalli):
        Veicolo.__init__(self, marca, modello)
        DotazioniSpeciali.__init__(self, dotazioni)
        self.cavalli = cavalli

    def mostra_info(self):
        super().mostra_info()
        print(f"Potenza: {self.cavalli}")
        self.mostra_dotazioni()

auto_sportiva = AutoSportiva(   "Ferrari", 
                                "F8", 
                                ["ABS", 
                                "Controllo Trazione" , 
                                "Airbag laterali"], 
                                720)

auto_sportiva.mostra_info()