# 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a - o produto do dobro do primeiro com metade do segundo .
# b - a soma do triplo do primeiro com o terceiro.
# c - o terceiro elevado ao cubo.

num1 = int(input("Informe um número inteiro: "))
num2 = int(input("Informe outro número inteiro: "))
real = float(input("Informe um número real: "))

print("a - o produto do dobro do primeiro com metade do segundo .")
print((num1 * 2) * (num2 / 2))

print("b - a soma do triplo do primeiro com o terceiro.")
print((num1 * 3) + real)

print("c - o terceiro elevado ao cubo.")
print(real ** 3)