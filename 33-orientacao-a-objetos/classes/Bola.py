class Bola():
    #CONSTRUTOR
    def __init__ (self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    #METODOS
    def trocaCor(self, nova_cor):
        self.cor = nova_cor;
    def mostraCor(self):
        return self.cor
    def trocaMaterial(self, novo_material):
        self.material = novo_material
    def mostraMaterial(self):
        return self.material

jabulani = Bola('Azul', 3, 'couro')
print(jabulani.mostraCor())
jabulani.trocaCor('Amarelo')
print(jabulani.mostraCor())
jabulani.trocaMaterial('plástico')
print(jabulani.mostraMaterial())