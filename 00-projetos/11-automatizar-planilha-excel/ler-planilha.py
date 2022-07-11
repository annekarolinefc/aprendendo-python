import openpyxl

#CARREGANDO ARQUIVO
book = openpyxl.load_workbook('Planilha de compras.xlsx')
#SELECIONANDO UMA PAGINA
frutas_page = book['Frutas']
#IMPRIMINDO OS DADOS DE CADA LINHA
for rows in frutas_page.iter_rows(min_row=2, max_row=5):
    for cell in rows:
        print(cell.value)
    #print(rows[0].value, rows[1].value, rows[2].value )