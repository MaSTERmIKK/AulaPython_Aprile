class Studente:
    def __init__(self, nome, voto):
        self.nome = nome
        self.__voto = voto
    
    @property
    def voto(self):
        print("voto getter")
        return self.__voto
    
    @voto.setter
    def voto(self, nuovo_voto):
        if(0 <= nuovo_voto <= 30):
            self.__voto = nuovo_voto
        else:
            print("voto non valido")

s = Studente("Emy", 8)
print(s.voto)
s.voto = -5
s.voto = 30
print(s.voto)
