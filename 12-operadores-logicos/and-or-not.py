a = 20
b = 17 
resto_a = a%2
resto_b = b%2 

if(resto_a==0 or resto_b==0):
    print("Ha um numero par.")
else:
    print("Nao ha um numero par.")

if(resto_a==0 or not resto_b>1):
    print("Ha um numero par.")
else:
    print("Nao ha um numero par.")
