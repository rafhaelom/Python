''' 
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule 
# e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a - salário bruto.
b - quanto pagou ao INSS.
c - quanto pagou ao sindicato.
d - o salário líquido.
e - calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
ganho_hora = float(input("Informe o quanto ganha por hora: "))
horas_trab = float(input("Informe o número de horas trabalhadas no mês (ex: 3.30) 3h e 30min: "))
salario_bruto = ganho_hora * horas_trab
ir = salario_bruto * (11 / 100)
inss = salario_bruto * (8 / 100)
sindicato = salario_bruto * (5 / 100)
salario_liquido = salario_bruto - (ir + inss + sindicato)
print(f"+ Salário Bruto : R$ {salario_bruto}")
print(f"- IR (11%) : R$ {ir}")
print(f"- INSS (8%) : R$ {inss}")
print(f"- Sindicato ( 5%) : R$ {sindicato}")
print(f"= Salário Liquido : R$ {salario_liquido}")