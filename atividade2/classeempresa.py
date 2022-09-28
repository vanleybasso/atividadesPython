class Cliente:
    def __init__(self, nome, sobrenome, cidade ):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cidade = cidade


class Dia:
    def __init__(self, cliente, banco, saldo):
        self.cliente = cliente
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
         
