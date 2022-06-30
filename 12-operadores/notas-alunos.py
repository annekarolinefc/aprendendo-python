primeiroBimestre = 5
if primeiroBimestre>10:
    print("Valor informado inválido.")

segundoBimestre = 9
if segundoBimestre>10:
    print("Valor informado inválido.")

terceiroBimestre = 8
if terceiroBimestre>10:
    print("Valor informado inválido.")

quartoBimestre = 6
if quartoBimestre>10:
    print("Valor informado inválido.")

media = (primeiroBimestre+segundoBimestre+terceiroBimestre + quartoBimestre)/4

if primeiroBimestre<=10 and segundoBimestre<=10 and terceiroBimestre<=10 and quartoBimestre<=10:
    print('Media: {}'.format(media))
else:
    print("Foi informado uma nota menor qie 10")