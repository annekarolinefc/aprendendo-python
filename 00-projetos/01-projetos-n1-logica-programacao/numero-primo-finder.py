# Verificar se o número é primo
# 2, 5, 7, 11, 13
# Número primo tem somente DOIS DIVISORES

numero = int(input("Digite um número e descubra se ele é primo:"))

if numero == 2 :
    print(f'{numero} é primo ')
elif numero%2 == 0 : #4
    print(f'{numero} não é primo ')
else :
    divisores = []
    for i in range(1, numero+1): #20
        if numero%i==0 :
            divisores.append(i)
            print(f'Dividores: {divisores}')
    if len(divisores) ==2 :  
        print(f'{numero} é primo ')
    else: 
        print(f'{numero} não é primo ')