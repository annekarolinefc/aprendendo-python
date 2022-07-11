arquivo = open("palavras.txt", "w") #Abri arquivo - leitura (nome do arquivo , modificador de acesso)
arquivo.write("Texto inserido a partir do código. \n")
arquivo.write("Inserindo nova frase. \n")
print(arquivo)
arquivo.close() #fecha o arquivo