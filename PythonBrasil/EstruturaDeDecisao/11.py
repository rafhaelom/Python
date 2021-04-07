'''11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe 
contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
baseado no salário atual:
- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
- o salário antes do reajuste;
- o percentual de aumento aplicado;
- o valor do aumento;
- o novo salário, após o aumento.'''

salarioAtual = float(input("Informe seu salário: "))
aumento_20 = 20/100
aumento_15 = 15/100
aumento_10 = 10/100
aumento_5 = 5/100

if(salarioAtual <= 280.00):
    print("O salário antes do reajuste: R$ {0:.2f}".format(salarioAtual))
    print("O percentual de aumento aplicado: {0:2.0%}".format(aumento_20))
    print("O valor do aumento: R$ {0:.2f}".format(salarioAtual * aumento_20))
    print("O novo salário, após o aumento: R$ {0:.2f}".format(salarioAtual + (salarioAtual * aumento_20)))
elif(salarioAtual >= 280.00 and salarioAtual <= 700.00):
    print("O salário antes do reajuste: R$ {0:.2f}".format(salarioAtual))
    print("O percentual de aumento aplicado: {0:2.0%}".format(aumento_15))
    print("O valor do aumento: R$ {0:.2f}".format(salarioAtual * aumento_15))
    print("O novo salário, após o aumento: R$ {0:.2f}".format(salarioAtual + (salarioAtual * aumento_15)))
elif(salarioAtual >= 700.00 and salarioAtual <= 1500.00):
    print("O salário antes do reajuste: R$ {0:.2f}".format(salarioAtual))
    print("O percentual de aumento aplicado: {0:2.0%}".format(aumento_10))
    print("O valor do aumento: R$ {0:.2f}".format(salarioAtual * aumento_10))
    print("O novo salário, após o aumento: R$ {0:.2f}".format(salarioAtual + (salarioAtual * aumento_10)))
elif(salarioAtual > 1500.00):
    print("O salário antes do reajuste: R$ {0:.2f}".format(salarioAtual))
    print("O percentual de aumento aplicado: {0:2.0%}".format(aumento_5))
    print("O valor do aumento: R$ {0:.2f}".format(salarioAtual * aumento_5))
    print("O novo salário, após o aumento: R$ {0:.2f}".format(salarioAtual + (salarioAtual * aumento_5)))
else:
    print("Valor incorreto!")