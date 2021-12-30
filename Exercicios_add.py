#GERAL
print(
    '1- ENCONTRA MAIOR NUMERO \n'+
    '2- ENCONTRA VALOR NEGATIVO \n'+
    '3- IMC \n'+
    '4- NOTA ENTRE 0 E 10 \n'+
    '5- INTERVALO ENTRE NUMEROS \n'+
    '6- NUMEROS IMPARES \n'+
    '7- 3 LADOS DE UM TRIANGULO \n'+
    '8- QUANTO GANHA POR HORA \n'
)
opcao = int(input('DIGITE O NUMERO CORRESPONDENTE AO EXERCICIO: ')) 
if opcao == 1:
#"Faça um Programa que peça dois números e imprima o maior deles."
    val1 = input('DIGITE O VALOR 1: ')
    val2 = input('DIGITE O VALOR 2: ')

    if val1 > val2:
        print(f'VALOR 1({val1}) é maior que valor 2({val2})')
    else:
        print(f'VALOR 2({val2}) é maior que valor 1({val1})')
################################################################################################################################
elif opcao == 2:
#"Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."
    val3 = int(input('DIGITE UM VALOR: '))
    if val3 < 0:
        print('VALOR NEGATIVO')
    else:
        print('VALOR POSITIVO')
###############################################################################################################################
elif opcao == 3:
#"Faça um Programa que calcule o IMC de uma pessoa. (peso / (altura * altura)"
    peso = float(input('DIGITE SEU PESO: '))
    altura = float(input('DIGITE SUA ALTURA: '))
    print('SEU IMC É: ',peso/(altura*altura))
###############################################################################################################################
elif opcao == 4:
#"Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido."    
    nota = 123456
    while nota < 0 or nota > 10:
        print('NOTA PRECISA ESTAR ENTRE 0 E 10')
        nota = float(input('DIGITE SUA NOTA(ENTRE 0 E 10): '))
##############################################################################################################################
elif opcao == 5:
#"Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles."
    num1 = int(input('DIGITE O 1º NUMERO: '))
    num2 = int(input('DIGITE O 2º NUMERO: '))
    for x in range(num1 , num2+1):
        print(x)
##############################################################################################################################
elif opcao == 6:        
#"Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50."
    for x in range(1,50,2):
        print(x)
##############################################################################################################################
elif opcao == 7:        
#"Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;"
    lado1 = float(input('DIGITE O LADO 1º LADO DO TRIANGULO: '))
    lado2 = float(input('DIGITE O LADO 2º LADO DO TRIANGULO: '))
    lado3 = float(input('DIGITE O LADO 3º LADO DO TRIANGULO: '))
    if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
        print('É UM EQUILATERO')
    elif (lado1 == lado2 and lado1 != lado3) or (lado2 == lado3 and lado2 != lado1) or(lado3 == lado1 and lado3 != lado2):
        print('É UM ISOSCELES')
    elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
        print('É UM ESCALENO')  
##############################################################################################################################
elif opcao == 8:        
#"Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
#  8% para o INSS e 5% para o sindicato."
#"Mostre na tela também o seu Salário bruto / Quanto pagou ao INSS / 
# Quanto pagou ao sindicato / Quanto pagou ao IR / O salário líquido." 
    ganhaPorHora = float(input('DIGITE QUANTO GANHA POR GANHA POR HORA: ')) 
    horaPorMes = float(input('DIGITE A QTD DE HORAS NO MES: '))    
    totalBruto = ganhaPorHora * horaPorMes
    descImpRenda = (totalBruto * 0.11) 
    descInss = (totalBruto * 0.08)
    descSind = (totalBruto * 0.05)
    totalLiquido = totalBruto -(descImpRenda+descInss+descSind)

    print(f'SALARIO BRUTO: {totalBruto} \n DESCIMPRENDA: {descImpRenda} \n DESCINSS: {descInss} \n DESCSIND: {descInss} \n SALARIO LIQUIDO: {totalLiquido}')
              