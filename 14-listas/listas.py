# CRIAR UMA LISTA
lista_numeros = [1, 2, 3,4]
lista_animais = ['cachorro', 'gato', 'elefante']
print(lista_numeros)
print(lista_animais)

# IMPRIMINDO A LISTA
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

# TUPLAS - imutável

# INTERAGIR COM TUPLAS

# CONVERSOES DE LISTAS E TUPLAS