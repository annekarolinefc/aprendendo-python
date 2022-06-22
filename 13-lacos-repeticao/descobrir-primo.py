a = 7

div=0
for x in range(1,a+1):
    resto = a%x 
    print(resto)
    if resto == 0:
        div = div + 1
if div==2:
    print("numero {} eh primo".format(a))
else:
    print("numero {} nao eh primo".format(a))