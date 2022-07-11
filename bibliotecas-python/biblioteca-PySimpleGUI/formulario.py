import PySimpleGUI as sg
class TelaPython:
    def __init__(self):
        #LAYOUT
        layout = [
            [sg.Text('Nome: ', size=(5,0)), sg.Input(size=(15,0), key='nome')],
            [sg.Text('Idade: ', size=(5,0)), sg.Input(size=(15,0), key='idade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Text('Aceita cartão?')],
            [sg.Radio('Sim', 'cartoes', key='aceitaCartao'), sg.Radio('Não', 'cartoes', key='naoAceitaCartao')],
            [sg.Slider(range=(0,100), default_value=0, orientation='h', size=(15,20), key='sliderVelocidade')],
            [sg.Button('Enviar')],
            [sg.Output(size=(30, 20))]
        ]
        #JANELA
        self.janela = sg.Window('Dados do usuario').layout(layout)


    def Iniciar(self):
        while True:
            # EXTRAIR OS DADOS DA TELA
            self.button, self.values = self.janela.read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail=self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao_sim=self.values['aceitaCartao']
            aceita_cartao_nao=self.values['naoAceitaCartao']
            velocidade_script = self.values['sliderVelocidade']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'aceita gmail: {aceita_gmail}')
            print(f'aceita outlook: {aceita_outlook}')
            print(f'aceita yahoo: {aceita_yahoo}')
            print(f'aceita cartao: {aceita_cartao_sim}')
            print(f'nao aceita cartao: {aceita_cartao_nao}')
            print(f'Velocidade: {velocidade_script}')

tela = TelaPython()
tela.Iniciar()