# Escreva um programa que peça uma nota entre 0 e 10. Mostre uma mensagem se o valor estiver inválido pedindo até que o usuário informe um valor válido.

print ("Olá! Seja Bem vindo!")

nota = int(input("Digite uma nota de 0 a 10: "))


while (nota >10) or (nota < 0):
    print ("Valor inválido!")
    nota = int(input("Atenção! Digite novamente um nota de 0 a 10: "))
    
else:
    print ("Sua nota é: ", nota)
