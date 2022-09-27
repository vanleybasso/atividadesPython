from classerempresa import Dia


empresadia = Dia ('EMPRESA ADS', 'NUBANK', 1000.0)
conta_fornecedor = Dia ('FORNCEDOR ADS', 'BANCO DO BRASIL', 500.0)

empresadia.extrato()
conta_fornecedor.extrato()

empresadia.transferencia_para (conta_fornecedor, float(input('Olá {}, digite o valor de transferência para a conta de {}:'. format(empresadia.titular, conta_fornecedor.titular))))

empresadia.extrato()
conta_fornecedor.extrato()
