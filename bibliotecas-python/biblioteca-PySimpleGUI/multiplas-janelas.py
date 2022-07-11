#pip install PySimpleGui

import PySimpleGUI as sg
#[ ] CRIAR AS JANELAS E ESTILOS - LAYOUT
#[ ] CRIAR AS JANELAS INICIAS
#[ ] CRIAR UM LOOP DE LEITURA DE EVENTOS
#[ ] LOGICA DE O QUE DEVE ACONTECER AO CLICAR OS BOTÕES

#CRIAÇÃO DAS JANELAS E ESTILOS
def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)
def janela_pedido():
    sg.theme('Reddit')
    layout=[
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('Pizza Pepperoni', key='pizza1'), sg.Checkbox('Pizza de Frango c/ Catupiry', key='pizza2')],
        [sg.Button('Voltar'), sg.Button('Fazer Pedido')]
    ]
    return sg.Window('Fazer Pedido', layout=layout, finalize=True)

#CRIAR AS JANELAS INICIAIS
janela1, janela2 = janela_login(), None

#CRIAR UM LOOP DE LEITURA DE EVENTOS
while True:
    window, event, values = sg.read_all_windows()
    #QUANDO A JANELA FOR FECHADA
    if window==janela1 and event ==sg.WIN_CLOSED:
        break
    #QUANDO QUEREMOS IR PARA A PROXIMA JANELA
    if window == janela1 and event=='Continuar':
        janela2 = janela_pedido()
        janela1.hide()
    if window == janela2 and event=='Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event=='Fazer Pedido':
        if values['pizza1'] == True and values['pizza2'] == True:
            sg.popup('Foram solicitados uma Pizza Pepperoni e uma Pizza Catupiri c/ Frango')
        if values['pizza1'] == True:
            sg.popup('Foram solicitados uma Pizza Pepperoni')
        if values['pizza2'] == True:
            sg.popup('Foram solicitados uma Pizza Catupiri c/ Frango')
        if values['pizza1'] == False and values['pizza2'] == False:
            sg.popup('Não foi solicitado nenhum pedido.')
    #QUANDO QUEREMOS VOLTAR PARA A JANELA ANTERIOR
