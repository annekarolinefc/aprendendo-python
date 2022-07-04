tupla = (('valor', 'chave'), ('nome', 'Matheus'), ('idade', 30))
print(tupla)
print(tupla[1][1])

dicionario = dict((x,y) for x,y in tupla)
print(dicionario)
print(dicionario['nome'])
print(dicionario['idade'])