print('BEM-VINDO A CALCULADORA DE MÉDIA')
nome_aluno = input('Digite o seu nome:')
nome_materia = input('Digite o nome da materia:')
nota_01 = float(input('Digite a 1º nota:'))
nota_02 = float(input('Digite a 2º nota:'))
nota_03 = float(input('Digite a 3º nota:'))
nota_04 = float(input('Digite a 4º nota:'))
media = (nota_01+nota_02+nota_03+nota_04)/4

if media<7:
    print(f'Aluno {nome_aluno}, você foi REPROVADO. Sua média em {nome_materia} foi {media}')
else:
    print(f'PARABÉNS!! \n Aluno {nome_aluno}, você foi APROVADO. Sua média em {nome_materia} foi {media}', )
    #print('PARABÉNS!! \n Aluno %s, você foi APROVADO. Sua média em %s foi %.2f')