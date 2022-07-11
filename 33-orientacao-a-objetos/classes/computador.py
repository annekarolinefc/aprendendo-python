#Marca, Memoria Ram, Placa de Video
class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram=memoria_ram
        self.placa_de_video = placa_de_video
    #METODOS: ligar, desligar, exibir configurações
    def Ligar(self):
        print('Estou ligando')
    def Desligar(self):
        print('Estou desligando')
    def ExibirInformacoesComputador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)
#INSTANCIAÇÃO
computador1= Computador('Asus', '8gb', 'Nvidia')
computador2 = Computador('Dell', '10gb', 'GeForce')
computador3 = Computador('Acer', '16gb', 'ATM')
#IMPRESSAO NO CONSOLE
print(computador1.marca)
print(computador2.marca)
print(computador3.marca)
print(computador1.Ligar())
print(computador1.Desligar())
print(computador1.ExibirInformacoesComputador())
'''
computador1= Computador()
computador2 = Computador()
computador3 = Computador()
print(computador1.marca, computador1.memoria_ram, computador1.placa_de_video)
print(computador2.marca, computador2.memoria_ram, computador2.placa_de_video)
print(computador3.marca, computador3.memoria_ram, computador3.placa_de_video)
'''