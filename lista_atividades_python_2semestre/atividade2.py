# 2) Faça um sistema bibliotecário: Printar uma lista com 10 livros; Pedir o nome de quem está solicitando; Escolher o livro; Printar o livro selecionado com o nome de quem solicitou.

class Livro:
    def __init__ (self, livro):
        self.livro = livro
        
 # Em outro arquivo

from livraria import Livro

livro_0 = Livro("Fogo & Sangue")
livro_1 = Livro("É assim que acaba")
livro_2 = Livro("Todas suas (im)perfeições")
livro_3 = Livro("Verity")
livro_4 = Livro("O homem mais rico da Babilônia")
livro_5 = Livro("Hobbit")
livro_6 = Livro("Saboroso cadáver")
livro_7 = Livro("A biblioteca da meia-noite")
livro_8 = Livro("Passaporte 2030")
livro_9 = Livro("Em busca de mim")

print("Bem-vindo(a) a Livraria ADS!")
cliente = input("Digite seu nome para fazer a reserva do livro: ")
print(cliente, "No momento temos 10 opções de livros: ",
"\n 0 - ", livro_0.livro, "\n 1 - ", livro_1.livro,"\n 2 -", livro_2.livro,"\n 3 -", livro_3.livro, "\n 4 - ", livro_4.livro, "\n 5 - ", livro_5.livro, "\n 6 - ", livro_6.livro,"\n 7 -", livro_7.livro,"\n 8 -", livro_8.livro, "\n 9 - ", livro_9.livro )

escolha = int(input("Selecione a opção desejada: "))

lista_livro = [livro_0, livro_1, livro_2, livro_3, livro_4, livro_5, livro_6, livro_7, livro_8, livro_9]

opcao_sel = int(escolha)

for opcao in lista_livro:
    if opcao_sel > 9:
        print("Atenção! Opção inválida!")
        break
    if opcao_sel <= 9:
        print(cliente, "seu livro reservado foi: ", lista_livro[opcao_sel].livro)
        print("Obrigado, volte sempre")
        break



