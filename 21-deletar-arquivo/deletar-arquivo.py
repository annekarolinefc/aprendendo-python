import os 

if os.path.exists("teste.txt"):
    os.remove("teste.txt")
else:
    print("O arquivo não existe!")