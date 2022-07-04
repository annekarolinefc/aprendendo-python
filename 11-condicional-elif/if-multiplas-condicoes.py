# Usuário pode ou não dirigir
cnh = True
idade = 21
idade_base = 18

if((cnh == True) and (idade >= idade_base)):
    print("Usuário pode dirigir um automovel.")
elif((cnh == False) and (idade >= idade_base)):
    print("Usuário nao pode dirigir um automovel. Não possui CNH.")
else:
    print("O usuário nao pode dirigir")