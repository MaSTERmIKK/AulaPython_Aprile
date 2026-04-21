class Automobile:

    numero_ruote = 4                    #attributo di classe

    def __init__(self, marca, modello): # Costruttore
        self.marca = marca              # Attributo di istanza
        self.modello = modello          # Attributo di istanza
    
    def stampa_info(self):
        print(f"L'automobile è una {self.marca} {self.modello}")