aluno = {
    # CHAVE E VALOR
    'nome' : 'Pedro Henrique',
    'nota' : 9.2,
    'ativo' : True
}

print(type(aluno))
print(aluno['nome'])
print(aluno['nota'])
print(aluno['ativo'])
print(len(aluno))

#Pessoas usando tuplas
pessoa1 = ("Nico", 39)
pessoa2 = ("Flavio", 37)
pessoa3 = ("Marcos", 30)

#Guardando as tuplas dentro de uma lista
instrutores = [pessoa1, pessoa2, pessoa3]

#imprimindo
print(instrutores)
print(instrutores[1][1])#idade do Flavio