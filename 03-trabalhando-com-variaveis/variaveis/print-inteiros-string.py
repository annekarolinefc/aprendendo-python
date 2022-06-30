# Primeiro erro em python
#!python3
texto = 'Sua idade é ... '
idade = 29
#print(texto + idade) -> ERRO
print(texto + str(idade))
print(f'{texto}{idade}')