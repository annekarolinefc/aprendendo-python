nome = 'Matheus'

# Escopo Local
if 'nome' in locals():
    print('A variável nome esta no escopo local')
    
# Escopo Global
if 'nome' in globals():
    print("A variavel nome esta no escopo local")
    
def teste():
    idade=18
    
    if 'idade' in locals():
        print("A variável idade esta no escopo local.")
teste()