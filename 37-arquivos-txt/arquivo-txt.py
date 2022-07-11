#COMO CRIAR E MODIFICAR ARQUIVOS:
valores_celulares = [850, 2230, 1500, 3500, 5000]

'''
BIBLIOTECA WRITE
'r' -> USANDO SOMENTE PARA LER ALGO
'w' -> USADO SOMENTE PARA ESCREVER ALGO
'r+' -> USADO SOMENTE PARA LER E ESCREVER ALGO
'a' -> USADO PARA ACRESCENTAR ALGO
'''

'''ESCREVENDO NO ARQUIVO TXT'''
with open('valores_celulares.txt', 'w') as arquivo:
    for valor in valores_celulares:
        arquivo.write(str(valor) + '\n')

'''METODO PARA NAO SOBRESCREVER OS RESULTADOS -> a'''
with open('valores_celulares.txt', 'a') as arquivo:
    for valor in valores_celulares:
        arquivo.write(str(valor) + '\n')

'''LENDO OS DADOS DO ARQUIVO TXT'''
with open('valores_celulares.txt', 'r') as arquivo:
    for valor in valores_celulares:
        print(valor)

'''LENDO OS DADOS DO ARQUIVO TXT E COLOCANDO LINHA ADICIONAL'''
with open('valores_celulares.txt', 'r+') as arquivo:
    for valor in valores_celulares:
        print(valor)
    arquivo.write('9000')