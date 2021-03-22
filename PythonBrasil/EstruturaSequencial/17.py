''' 17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados 
da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que 
a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre 
arredonde os valores para cima, isto é, considere latas cheias.
'''
cobertura_tinta = 6
lata_litros = 18
preco_lata = 80
galao_litros = 3.6
preco_galao = 25

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
tamanho = int(input("Qual o tamanho da área a ser pintada em metros quadrados: "))
total_litros = tamanho / cobertura_tinta
print(f"Quantidade de litros a comprar: {total_litros} litros")

# comprar apenas latas de 18 litros;
q_latas = total_litros / lata_litros
pagar_lata = q_latas * preco_lata
print(f"Quantidade de latas a comprar: {q_latas} latas de 18 litros")
print(f"O valor das latas é: R$ {pagar_lata}")

# comprar apenas galões de 3,6 litros;
q_galao = total_litros / galao_litros
pagar_galao = q_galao * preco_galao
print(f"Quantidade de latas a comprar: {q_galao} latas de 18 litros")
print(f"O valor das latas é: R$ {pagar_galao}")

# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga
# e sempre arredonde os valores para cima, isto é, considere latas cheias.
latas_cheias = total_litros + (10 / 100)
print(f"Acrescimo de 10% é {latas_cheias}")
q_t_acrescimo = latas_cheias / cobertura_tinta
print(f"Litros de latas e galões cheios {q_t_acrescimo}")
q_latas_galao = q_t_acrescimo / (lata_litros + galao_litros)
preco_menor = q_latas_galao * (preco_lata + preco_galao)
print(f"O preço menor é R$ {preco_menor}")