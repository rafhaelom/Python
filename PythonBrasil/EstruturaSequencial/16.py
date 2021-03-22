# 16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados 
# da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades 
# de latas de tinta a serem compradas e o preço total.

cobertura = 3
capacidade_lata = 18
custo_lata = 80

tamanho = int(input("Qual o tamanho da área a ser pintada em metros quadrados: "))

quantidade_litro = tamanho / cobertura
latas = int(quantidade_litro / capacidade_lata)

print(f"Precisará de {latas} latas de tintas de 18 litros.")
print(f"Total ficará em: R$ {latas * custo_lata}")
