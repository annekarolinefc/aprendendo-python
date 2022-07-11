import random #importando o modulo

numero_secreto = round(random.random() * 100)
print(numero_secreto)

numero_secreto_dois = random.randrange(1, 101)
print(numero_secreto_dois)


#Quando nao se passa parâmetro supoe que você quer dizer de zero até número passado -1. 
# menor: 0
# maior: 9
aleatorio = random.randrange(10)
print(aleatorio)