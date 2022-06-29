# O usuario ira entrar com uma texto e com uma letra
# Contar a quantidade de vezes que essa letra aparece

texto = str(input("Insira uma palavra: "))
letra = str(input("Insira uma letra: "))
frequencia = 0

for i in texto : #percorrer todo o texto 
    print(i)
    if(i == letra) :
        frequencia+=1
print(f'A letra {letra} aparece {frequencia} vezes no texto {texto}')