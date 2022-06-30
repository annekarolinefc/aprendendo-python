# Não tem constantes em Python. Existe uma convensão: Letras maisuculas
PI = 3.14
raio = input('Informe o raio da circunferencia: ')
print(type(raio)) #É UMA STRING
raioFloat = float(input('Informe o raio da circunferencia: '))#CONVERTE PARA DOUBLE
print(type(raioFloat)) #É UM FLOAT

area = PI * raioFloat * raioFloat
print(area)
 