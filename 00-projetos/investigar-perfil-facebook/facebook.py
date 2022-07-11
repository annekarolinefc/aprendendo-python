#VARIAVEIS
codigo_facebook = 1240594666
urls_com_id = []
urls_sem_id = ['https://facebook.com/search/%s/photos-of']
descricao = ['Verificando fotos bloqueadas']

#FUNÇÕES
#FUNÇÃO INSERIR CORIGO NA URL
for url in urls_sem_id:
    urls_com_id.append(urls_sem_id % codigo_facebook)

#FUNÇÃO RESULTADO
for x in range(len(descricao)):
    print(descricao[x])
    print(urls_com_id[x])
    print('')

#VERIFICANDO FOTOS BLOQUEADAS
#https://facebook.com/search/ID/photos-of