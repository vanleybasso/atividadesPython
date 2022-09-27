class Dia:
    def __init__(self, titular, banco, saldo):
        print("Finalizando saldo do caixa no dia")
        self.titular = titular
        self.saldo = saldo
        self.banco = banco 

    def venda(self, valor):
        self.saldo += valor
        
    def compra(self, valor):
        if (self.saldo < valor):
            print ("Saldo indisponível no caixa, você não consegue realizar compras nesse valor no dia de hoje!")
        else:
         self.saldo -= valor

    def transferencia_para (self, contadestino, valor):
        if (self.saldo < valor):
            print ("Saldo insuficiente para realizar a transferência!")
            return False
        retirou = self.compra(valor)
        if (retirou == False):
            return False 
        else:
            contadestino.venda(valor)
            return True
         

   

    def extrato(self):
        print ('titular: {} \nbanco: {} \nsaldo: {}'. format(self.titular, self.banco, self.saldo))
