# Você terá que criar um programa para mostrar os dias da semana correspondente ao seu número, exemplo: 1 == Domingo, 2 == Segunda, etc.

nome = input("Olá, digite seu nome:")
print ("Seja bem vindo", nome.title()) 

dia = int(input("Vamos descobrir que dia é hoje! Digite o dia da semana:"))

if (dia == 1):
    print ("Hoje é domingo!")

if (dia == 2):
    print ("Hoje é segunda-feira!")
    
if (dia == 3):
    print ("Hoje é terça-feira!")
    
if (dia == 4):
    print ("Hoje é quarta-feira!")
    
if (dia == 5):
    print ("Hoje é quinta-feira!")
    
if (dia == 6):
    print ("Hoje é sexta-feira!")
    
if (dia == 7):
    print ("Hoje é sábado!")

elif (dia >7):
    print ("Dia inválido!")
