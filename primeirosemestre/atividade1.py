# Escreva um programa onde você terá que mostrar na tela o tempo de um download para o usuário. Para isso você terá que calcular o tamanho do arquivo que será baixado (em MB) e a velocidade do link da Internet que está sendo usada (em Mbps). Calcule utilizando da função matemática MULTIPLICAÇÃO e mostre o tempo que será necessário para o download em minutos

print ("Vamos realizar o dowload!")

tamanho = float(input("Digite o tamanho do arquivo em MB:"))
velocidade = float(input("Digite a velocidade Mbps:"))

tempo =(tamanho * velocidade) /60

print ("O tempo aproximado é de:", round(tempo,2), "minutos")
