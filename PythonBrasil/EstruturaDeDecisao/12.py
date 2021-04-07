''' 
12 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do 
Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e 
que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao 
usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
- Salário Bruto até 900 (inclusive) - isento
- Salário Bruto até 1500 (inclusive) - desconto de 5%
- Salário Bruto até 2500 (inclusive) - desconto de 10%
- Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme 
o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
'''

valorHora = float(input("Informe o valor da sua hora: "))
qtHorasTrab = int(input("Informe suas horas trabalhadas no mês: "))

salarioBruto = valorHora * qtHorasTrab
des_5 = 5/100
des_10 = 10/100
des_11 = 11/100
des_20 = 20/100

print("\n")

if (salarioBruto <= 900.00):
    print("Salário Bruto \t\t: R$ {0:.2f}".format(salarioBruto))
    print("(-) IR (isento) \t: R$ {0:.2f}".format(0))
    print("(-) INSS ( 10%) \t: R$ {0:.2f}".format(salarioBruto * des_10))
    print("FGTS (11%) \t\t: R$ {0:.2f}".format(salarioBruto * des_11))
    print("Total de descontos \t: R$ {0:.2f}".format((salarioBruto * des_5) + (salarioBruto * des_10)))
    print("Salário Liquido \t: R$ {0:.2f}".format(salarioBruto - ((salarioBruto * des_5) + (salarioBruto * des_10))))
elif (salarioBruto > 900.00 and salarioBruto <= 1500.00):
    print("Salário Bruto: R$ {0:.2f}".format(salarioBruto))
    print("(-) IR (5%): R$ {0:.2f}".format(salarioBruto * des_5))
    print("(-) INSS ( 10%): R$ {0:.2f}".format(salarioBruto * des_10))
    print("FGTS (11%): R$ {0:.2f}".format(salarioBruto * des_11))
    print("Total de descontos: R$ {0:.2f}".format((salarioBruto * des_5) + (salarioBruto * des_10)))
    print("Salário Liquido: R$ {0:.2f}".format(salarioBruto - ((salarioBruto * des_5) + (salarioBruto * des_10))))
elif (salarioBruto > 1500.00 and salarioBruto <= 2500.00):
    print("Salário Bruto: R$ {0:.2f}".format(salarioBruto))
    print("(-) IR (10%): R$ {0:.2f}".format(salarioBruto * des_10))
    print("(-) INSS ( 10%): R$ {0:.2f}".format(salarioBruto * des_10))
    print("FGTS (11%): R$ {0:.2f}".format(salarioBruto * des_11))
    print("Total de descontos: R$ {0:.2f}".format((salarioBruto * des_10) + (salarioBruto * des_10)))
    print("Salário Liquido: R$ {0:.2f}".format(salarioBruto - ((salarioBruto * des_10) + (salarioBruto * des_10))))
elif (salarioBruto > 2500.00):
    print("Salário Bruto: R$ {0:.2f}".format(salarioBruto))
    print("(-) IR (20%): R$ {0:.2f}".format(salarioBruto * des_20))
    print("(-) INSS ( 10%): R$ {0:.2f}".format(salarioBruto * des_10))
    print("FGTS (11%): R$ {0:.2f}".format(salarioBruto * des_11))
    print("Total de descontos: R$ {0:.2f}".format((salarioBruto * des_20) + (salarioBruto * des_10)))
    print("Salário Liquido: R$ {0:.2f}".format(salarioBruto - ((salarioBruto * des_20) + (salarioBruto * des_10))))
else:
    print("Valor incorreto!")