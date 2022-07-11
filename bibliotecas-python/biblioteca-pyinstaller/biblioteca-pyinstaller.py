#pip install pyinstaller
#pyinstaller --onefile nome-do-arquivo

nome = input('Digite o seu nome:')
idade = int(input('Digite sua idade:'))

print(('Olá {}, você possui {} anos.').format(nome, idade))