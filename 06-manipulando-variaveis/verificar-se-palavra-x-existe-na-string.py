# Verificar se string contém uma palavra em Python
frase = 'O rato roeu a roupa do rei de Roma.'
print(frase)

palavra = 'rato'

if palavra not in frase:
    print("A frase não contem a palavra: " + palavra)
else:
    print("A frase contem a palavra: " + palavra)
    
# Outra alternativa para fazer:
if frase.count(palavra) == 0:
    print("A frase não contem a palavra: " + palavra)
else:
    print("A frase contem a palavra: " + palavra)