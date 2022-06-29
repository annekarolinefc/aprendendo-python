#NUMERO GUESS - Adivinhar numero
# O algoritmo vai gerar o numero (0 a 10) e temos que adivinhar
# contar tentativas

import random

numero = random.randint(0, 10)
tentativa = 1
#tentativa = 3; Você tem somente 3 tentativas

while True:
    guess = int(input("Adivinhe o número:"))
    if numero == guess :
        print(f'Você adivinhou o numero {numero} na {tentativa} tentativa.')
        break
    tentativa+=1
    #tentaiva-=1
    
