# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:a) "Telefonou para a vítima?" b) "Esteve no local do crime?" c) "Mora perto da vítima?"d) "Devia para a vítima?" e) "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Casocontrário, ele será classificado como "Inocente".


nome = input("Olá, digite seu nome:")
print ("Seja bem vindo", nome.title())


print ("Vamos começar o questionário!")
print ("1- Você telefonou para a vítima?")
menu1 = int(input("1. Sim - 0. Não \n"))

print ("2- Você esteve no local do crime?")
menu2 = int(input("1. Sim - 0. Não \n"))

print ("3- Mora perto da vítima?")
menu3 = int(input("1. Sim - 0. Não \n"))

print ("4- Devia algo para a vítima?")
menu4 = int(input("1. Sim - 0. Não \n"))

print ("5- Devia algo para a vítima?")
menu5 = int(input("1. Sim - 0. Não \n"))

soma = (menu1 + menu2 + menu3 + menu4 + menu5)

if (soma == 2):
    print ("Você foi considerado(a) suspeito(a)!")

elif (soma == 3) or (soma == 4) :
    print ("Você foi considerado cúmplice!")
    
elif (soma == 5):
    print ("Você foi considerado(a) culpado(a)")
    
