parola = "" # Variabile Globale

class Computer:
    def __init__(self, processore):
        self.__processore = processore #Atttributo privato
    
    def get_processore(self):
        parola = "pippo" # Variabili locali
        return self.__processore
    
    def set_processore(self, processore):
        parola = 22 # Variabili locali
        self.__smonta()
        self.__processore = processore
    
    def __smonta(self):
        print("Camputer smontato")


c = Computer("Intel Ultra 7")

print(c.get_processore())
print(parola)
# c.set_processore("AMD Ryzen 7")
# print(c.get_processore())
# c.__processore = "Processore Nuovo"
