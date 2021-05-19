# 14 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento 
# diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido 
# pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de 
# R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável 
# peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos 
# além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do 
# programa com as mensagens adequadas.

limite_peso = 50.00
valor_multa = 4.00
peso = float(input("Informe o Peso de Peixes: "))
if (peso > limite_peso):
    excesso = float(peso - limite_peso)
    multa = float(valor_multa * excesso)
    print(f"Peso excedeu o limite de 50.00 Kg, o excesso foi de: {excesso}Kg")
    print(f"João você deverá pagar uma multa de R${multa}")
else:
    print(f"Peso esta dentro do limite, o peso foi de: {peso}Kg")