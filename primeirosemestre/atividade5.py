# Um posto está vendendo combustíveis com a seguinte tabela de descontos:a) Álcool:b) até 20 litros, desconto de 3% por litro c) acima de 20 litros, desconto de 5% por litro d) Gasolina: e) até 20 litros, desconto de 4% por litro f) acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

print ("Olá. Seja bem vindo ao Posto ADS!")


menu = input("Deseja a opção para abastecer: a. Alcool - g. Gasolina \n")

    
    
if (menu == "a"):
    alcoollt = int(input("Digite quantos litros de alcool você deseja abastecer: "))
    if (alcoollt < 21):
        valorfinal = (alcoollt * 1.90) 
        desconto = (alcoollt * 1.90) * 0.03
        valorfinal2 = (valorfinal - desconto)
        print ("O valor total no abastecimento de alcool foi de: R$ %.3f " % valorfinal2)
    
    elif (alcoollt > 20):
        valorfinal= (alcoollt * 1.90) 
        desconto = (alcoollt * 1.90) * 0.05
        valorfinal2 = (valorfinal - desconto)
        print ("O valor total no abastecimento de alcool foi de: R$ %.3f " % valorfinal2)

if (menu == "g") :
    gasolinalt = int(input("Digite quantos litros de gasolina você deseja abastecer: "))
    if (gasolinalt < 21):
        precofinal = (gasolinalt * 2.50)
        desconto = (gasolinalt * 2.50) * 0.04
        precofinal2 = (precofinal - desconto)
        print ("O valor total no abastecimento de gasolina foi de: R$ %.3f " % precofinal2)
        
    elif (gasolinalt > 20):
        precofinal = (gasolinalt * 2.50)
        desconto = (gasolinalt * 2.50) * 0.06
        precofinal2 = (precofinal - desconto)
        print ("O valor total no abastecimento de gasolina foi de: R$ %.3f " % precofinal2)
        
    
