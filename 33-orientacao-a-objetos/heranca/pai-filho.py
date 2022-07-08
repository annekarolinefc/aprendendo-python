class Pai:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

class Filha(Pai):
    def __init__(self, nome, peso, cabelo):
        super().__init__(nome, peso)
        self.cabelo = cabelo

pessoa1 = Pai('Luiz', 65)
filha1 = Filha('Anne', 29, 'Castanho')
print(filha1.nome)
print(filha1.peso)
print(filha1.cabelo)