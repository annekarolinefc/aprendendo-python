#ENUMERATE
#ENUMERA ELEMENTOS DA LISTA
#ITERAVEIS

string = 'O Brasil é penta.'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])