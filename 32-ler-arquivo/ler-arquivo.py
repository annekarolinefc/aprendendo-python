arquivo = open("palavras.txt", "r") #modificador de leitura
#arquivo.write() não é permitido
for linha in arquivo:
    print(linha, end="\n")
#arquivo.read()
arquivo.close()

#LER APENAS A PRIMEIRA LINHA DO ARQUIVO
#linha = arquivo.readline()
#print(linha)