'''Criar uma função que me lembre a parar de estudar e fazer uma pausa a cada 2h
Trabalho inicia de 8h as 12h'''

#FUNÇÃO TIME E FUNÇÃO WEBBROWSER
import webbrowser
import time

intervalos = 2
contador = 0
print('O programa de controle de descanso foi ativado.')

while(contador<intervalos):
    time.sleep(10) #recebe o tempo em segundos
    #ABRIR VIDEO DO YOUTUBE
    webbrowser.open('https://www.youtube.com/watch?v=nSDgHBxUbVQ')
    contador = contador+1

