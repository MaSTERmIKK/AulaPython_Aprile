class Persona:

    def __init__(self, nome: str, eta: int):
        self.nome = nome
        self.eta = eta

    @classmethod
    def init_from_string(cls, s: str): 
        nome, eta = s.split(",") #stringa in arrivo "Mario,30"
        return cls(nome, int(eta))
    
p = Persona.init_from_string("Mario,30")
print(p.nome, p.eta)