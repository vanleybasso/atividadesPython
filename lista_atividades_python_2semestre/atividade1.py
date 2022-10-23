# 1) Crie um sistema para criação de pacotes de viagem onde você pedirá o nome de quem irá viajar, mostrar as opções e printar a que foi escolhida.

class Pacote_viagem:
    def __init__ (self, viagem):
        self.viagem = viagem

 # Em outro arquivo

from pacote import Pacote_viagem

pacote_0 = Pacote_viagem("Hungria")
pacote_1 = Pacote_viagem("Espanha")
pacote_2 = Pacote_viagem("Grécia")
pacote_3 = Pacote_viagem("Brasil")
pacote_4 = Pacote_viagem("Estados Unidos")

print("BEM VINDO(A)! Temos algumas ofertas com pacotes de viagens para você amigo cliente")

cliente = input("Caro cliente, para iniciarmos digite seu primeiro nome: ")
print(cliente, "temos 5 opções de pacotes para você escolher:", 
"\n 0- ", pacote_0.viagem, "\n 1- ", pacote_1.viagem, "\n 2- ", pacote_2.viagem, "\n 3- ", pacote_3.viagem, "\n 4- ", pacote_4.viagem)

escolha = int(input("Selecione a opção desejada: "))

lista_viagem = [pacote_0, pacote_1, pacote_2, pacote_3, pacote_4]

opcao_escolha = int(escolha)

for opcao in lista_viagem:
    if opcao_escolha >= 5:
        print("Atenção! Opção inválida!")
        break
    if opcao_escolha <= 4:
        print(cliente, ',seu pacote de viagem escolhido foi para o(a)', lista_viagem[opcao_escolha].viagem)
        print ("OBRIGADO PELA COMPRA E UMA ÓTIMA VIAGEM! ATÉ BREVE")
        break
