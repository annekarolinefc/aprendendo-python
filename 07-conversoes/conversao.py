a = 10
b = 5
soma = a + b
subtracao = a - b
print(soma)
print(type(soma))
soma = str(soma) #transformando int em string
print(type(soma))

print("Concatenacao")
print('soma: {}'.format(soma)) #utilizando format
print('soma:' + soma) 
print('Soma: {soma} \nSubtracao: {subtracao}'.format(soma=soma, subtracao=subtracao))