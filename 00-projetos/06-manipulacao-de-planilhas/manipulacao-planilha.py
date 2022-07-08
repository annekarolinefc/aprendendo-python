import csv

with open('teste.csv', 'w') as csvfile:
    cabecalho = ['id', 'num']
    escrita = csv.DictWriter(csvfile, fieldnames=cabecalho)
    escrita.writeheader()
    for r in range(10):
        escrita.writerow({'id':r, 'num': r+1})