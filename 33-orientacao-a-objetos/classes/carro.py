class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.nivel_combustivel= 0
    def andar(self, km):
        consumo = km/self.consumo
        self.nivel_combustivel -= consumo
    def obterGasolina(self):
        return self.nivel_combustivel
    def adicionarGasolina(self, gasolina):
        self.nivel_combustivel = self.nivel_combustivel + gasolina

meuSedan = Carro(10)
meuSedan.adicionarGasolina(20)
meuSedan.andar(10)
print(meuSedan.obterGasolina())