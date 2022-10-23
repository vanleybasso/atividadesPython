# 4) Criar um sistema de Agenda com POO;

class Contato:
    def __init__ (self, contato, telefone):
        self.contato = contato
        self.telefone = telefone
        
#Em outro arquivo
from contatos import Contato

contato_0 = Contato("Lucas", "54991477898")
contato_1 = Contato("Vanley", "54996214447")
contato_2 = Contato("Iuri", "54994791524")
contato_3 = Contato("Francis", "5499147624797")
contato_4 = Contato("Eliedson", "5499147791489")

print("Bem-vindo(a) a lista de contatos ADS!")
cliente = input("Digite seu nome para iniciarmos: ")
print(cliente, "Sua lista possui os seguintes contatos: ",
"\n 0 - ", contato_0.contato, "\n 1 - ", contato_1.contato,"\n 2 -", contato_2.contato,"\n 3 -", contato_3.contato, "\n 4 - ", contato_4.contato)

selecao = int(input("Selecione a opção desejada: "))

lista_contato = [contato_0, contato_1, contato_2, contato_3, contato_4]

opcao_sel = int(selecao)

for opcao in lista_contato:
    if opcao_sel >= 5:
        print("Atenção! Opção inválida!")
        break
    if opcao_sel <= 4:
        print(cliente, "o contato que você escolheu foi: ", lista_contato[opcao_sel].contato, "- Telefone:" , lista_contato[opcao_sel].telefone )
        print("Até breve!")
        break




        
