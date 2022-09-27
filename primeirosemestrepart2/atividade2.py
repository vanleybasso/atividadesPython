# Faça um programa que leia e valide as seguintes informações: a) Nome: maior que 3 caracteres; b) Idade: entre 0 e 150; c) Salário: maior que zero; d) Sexo: 'f' ou 'm';e) Estado Civil: 's', 'c', 'v', 'd';


print ('Olá, seja bem vindo! \n')



nome = str(input("Digite seu nome (mais que 3 caracteres): "))
while ( len(nome) <=  3 ):
	nome=str(input("Digite seu nome (mais que 3 caracteres): "))
else:
    print ("Seu nome é", nome.title())
	
	
idade = int(input("Digite sua idade (entre 0 e 150):"))
while ( idade > 150 ) or (idade < 0):
	idade=int(input("Digite sua idade (entre 0 e 150): "))
else:
    print ("Sua idade é", idade)
	
salario = float(input("Digite seu salário (maior que 0) : "))
while ( salario <= 0 ):
	salario=float(input("Digite seu salário (maior que 0) "))
else:
    print ("Seu salário é igual: R$ ", salario)

sexo = str(input("Digite a inicial do seu sexo - m. Masculino - f. Feminino:\n  "))
while  (sexo !="f") and (sexo!="m") :
	sexo = str(input("Digite a inicial do seu sexo-  m. Masculino - f. Feminino \n "))
else:
    print ("Seu sexo é", sexo)
	
estado_civil =  str(input("Digite a inicial do seu estado civil: s. Solteiro - c. Casado - v. Viúvo - d. Divorciado \n"))
while ( estado_civil != "s") and (estado_civil != "c") and (estado_civil != "v") and (estado_civil != "d" ):
	estado_civil= str(input("Digite a inicial do seu estado civil:s. Solteiro - c. Casado - v. Viúvo - d. Divorciado \n "))
else:
    print ("Seu estado civil é", estado_civil)
