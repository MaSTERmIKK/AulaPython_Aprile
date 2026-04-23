class Animale:
    def __init__(self, nome):
        self.nome = nome

    def fai_verso(self):
        print(f"{self.nome} fa un verso generico")

class Cane(Animale):

    def __init__(self, nome):
        super().__init__(nome)

    def fai_verso(self):
        print(f"{self.nome} sta abbaiando")

class Gatto(Animale):

    def fai_verso(self):
        print(f"{self.nome} sta miagolando")

animale = Animale("Pippo")
cane = Cane("Fido")
gatto = Gatto("Morfeo")

animale.fai_verso()
cane.fai_verso()
gatto.fai_verso()