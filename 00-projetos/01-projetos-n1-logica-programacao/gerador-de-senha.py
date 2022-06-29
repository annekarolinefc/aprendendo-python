# gerar uma senha segura - 12 caracteres - 3 Maiusculas, 3 minusculas, 3digitos, 3pontos
# salvar a senha em um arquivo

import string
import random
import time

maiuscula = random.choices(string.ascii_uppercase, k=3)
minuscula = random.choices(string.ascii_lowercase, k=3)
digitos = random.choices(string.digits, k=3)
ponts = random.choices(string.punctuation, k=3)

#senha = maiuscula + minuscula + digitos + ponts
senha = random.sample(maiuscula + minuscula + digitos + ponts, 12) #embaralhando 
senha_segura = ''.join(senha)
print(senha)
print(senha_segura)

horario = time.strftime('%d/%m/%Y %H:%M:%S')
with open('senha.txt', 'a') as file :
    file.write(f'A senha foi gerada {horario} \n')
    file.write(f'{senha_segura} \n')

#Salvando em um arquivo
