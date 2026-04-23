class Animale:
    def __init__(self, nome):
        self.nome = nome

    def fai_verso(self):
        print(f"{self.nome} fa un verso generico")

class Cane(Animale):

    def __init__(self, nome, eta):
        super().__init__(nome)
        self.eta = eta

    def fai_verso(self):
        print(f"{self.nome} sta abbaiando")

class Gatto(Animale):

    def __init__(self, nome, lenArtigli):
        super().__init__(nome)
        self.lenArtigli = lenArtigli

    def fai_verso(self, ):
        print(f"{self.nome} sta miagolando")

animale = Animale("Pippo")
cane = Cane("Fido", 10)
gatto = Gatto("Morfeo", 2.6)

animale.fai_verso()
cane.fai_verso()
gatto.fai_verso()