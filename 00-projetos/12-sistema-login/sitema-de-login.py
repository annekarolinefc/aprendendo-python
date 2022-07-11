#pip install pysimplegui
import PySimpleGUI as sg

#LAYOUT DA JANELA
layout=[
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('Login')],
    [sg.Text('', key='mensagem')]
]

#INSTANCIANDO A JANELA
window = sg.Window('Login', layout=layout)

#EVENTOS
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Login':
        senha_correta = '123456'
        usuario_correto= 'root'
        usuario = values['usuario']
        senha = values['senha']
        if senha ==senha_correta and usuario == usuario_correto:
            #alterar texto
            window['mensagem'].update("Login feito com sucesso")
        else:
            window['mensagem'].update("Senha ou usuário incorreto")