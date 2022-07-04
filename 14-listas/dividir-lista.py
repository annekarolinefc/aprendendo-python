lista = range(1, 100, 1)

def listaMenores(lista, n):
    for i in range(0, len(lista), n):
        yield lista[i:i+n]

listaDividida = list(listaMenores(lista, 10))
print(listaDividida)
