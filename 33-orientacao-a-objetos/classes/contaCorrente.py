class ContaCorrente():
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome
    def depositar(self, valor_deposito):
        self.saldo+=valor_deposito
    def sacar(self, valor_saque):
        self.saldo-=valor_saque
    def extrato(self):
        return f'Seu saldo atual é de {self.saldo}'

conta1 = ContaCorrente('1234', 'Anne')
conta1.depositar(1000)
print(conta1.extrato())