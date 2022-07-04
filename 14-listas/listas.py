# CRIAR UMA LISTA
lista_numeros = [1, 2, 3, 4]
lista_animais = ['cachorro', 'gato', 'elefante']

#Imprimir o tipo
print(type(lista_numeros)) #<class 'list'>
print(type(lista_animais)) #<class 'list'>

#Imprimir a lista
print(lista_numeros)
print(lista_animais)

#adicionar um elemento
lista_numeros.append(5)
lista_numeros.append(5) #Lista aceita repetição
print(lista_numeros)

#verificar tamanho da lista
print(len(lista_numeros))

#alterando elemento
lista_numeros[5] = 6
print(lista_numeros[5])
print(lista_numeros)
#ou
lista_numeros.insert(6, -700)
print(lista_numeros)

# IMPRIMINDO A LISTA - percorrendo os elementos
for x in lista_numeros:
    print(x)
# MANIPULAR UMA LISTA
    #soma
soma = 0
for x in lista_numeros:
    print(x)
    soma+=x
print(soma)

print(sum(lista_numeros))

    #maior valor
print(max(lista_numeros))

    #verificar se existe elemento
if 'gato' in lista_animais:
    print('Existe gato na lista')
else:
    print("não existe gato na lista")

    #adicionando elemento
lista_animais.append('lobo')
print(lista_animais)
    #removendo elemento
lista_animais.pop()
print(lista_animais)

lista_animais.pop(0)
print(lista_animais)

lista_animais.remove('elefante')
print(lista_animais)


# Lista para string
minhaLista = ['Python', 'é', 'muito', 'legal']
print(minhaLista)
minhaString = ' '.join(minhaLista) #separador de espaço + join + o elemento dentro do ()
print(minhaString)


# TUPLAS - imutável

# INTERAGIR COM TUPLAS

# CONVERSOES DE LISTAS E TUPLAS