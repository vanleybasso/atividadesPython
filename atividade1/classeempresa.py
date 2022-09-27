class Dia:
    def __init__(self, titular, banco, saldo):
        print("Finalizando saldo do caixa no dia")
        self.titular = titular
        self.saldo = saldo
        self.banco = banco 

    def venda(self, valor):
        self.saldo += valor
        
    def compra(self, valor):
        self.saldo -= valor
            
        
        
        
    def extrato(self):
        print ('titular: {} \nbanco: {} \nsaldo: {}'. format(self.titular, self.banco, self.saldo))
