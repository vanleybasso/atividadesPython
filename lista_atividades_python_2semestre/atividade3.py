#3) Criar um sistema de Feirinha (Vendas): Printar uma lista com as frutas; Pedir para quem está comprando inserir o nome; Após isso, pedir para selecionar a fruta; Após isso imprimir o nome do solicitante e a fruta.

class Fruta:
    def __init__ (self, fruta):
        self.fruta = fruta

#Em outro arquivo
from listafruta import Fruta

fruta_0 = Fruta("Maçã")
fruta_1 = Fruta("Laranja")
fruta_2 = Fruta("Melancia")
fruta_3 = Fruta("Uva")
fruta_4 = Fruta("Abacaxi")

print("Bem-vindo(a) a Fruteira ADS! Temos algumas ofertas para você!")
cliente = input("Digite seu nome para iniciarmos: ")
print(cliente, "Temos algumas promoções especiais hoje ",
"\n 0 - ", fruta_0.fruta, "\n 1 - ", fruta_1.fruta,"\n 2 -", fruta_2.fruta,"\n 3 -", fruta_3.fruta, "\n 4 - ", fruta_4.fruta)

selecao = int(input("Digite a opção desejada: "))

lista_fruta = [fruta_0, fruta_1, fruta_2, fruta_3, fruta_4]

opcao_sel = int(selecao)

for opcao in lista_fruta:
    if opcao_sel >= 5:
        print("Atenção! Opção inválida")
        break
    if opcao_sel <= 4:
        print(cliente, "a fruta que você escolheu foi:", lista_fruta[opcao_sel].fruta)
        print("Obrigado, volte sempre")
        break


