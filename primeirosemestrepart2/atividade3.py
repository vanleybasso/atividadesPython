# Escreva um programa que leia 5 números e informe o maior número.

print ("Olá, seja bem vindo!")

nota1 = int(input("Digite o primeiro número:"))
nota2 = int(input("Digite o segundo número:"))
nota3 = int(input("Digite o terceiro número:"))
nota4 = int(input("Digite o quarto número:"))
nota5 = int(input("Digite o quinto número:"))

if (nota1 > nota2 and nota3 and nota4 and nota5):
    print ("o maior número é o", nota1)

elif (nota2 > nota3 and nota4 and nota5):
    print ("o maior número é o", nota2)
    
elif (nota3 > nota4 and nota5):
    print ("o maior número é o", nota3)
    
elif (nota4 > nota5):
    print ("o maior número é o", nota4)
else:
    print ("o maior número é o", nota5)
    
