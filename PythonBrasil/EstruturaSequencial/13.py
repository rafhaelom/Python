# 13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo 
# que calcule seu peso ideal, utilizando as seguintes fórmulas:
# a - Para homens: (72.7*h) - 58
# b - Para mulheres: (62.1*h) - 44.7

h = float(input("Digite sua altura: "))
homens = float((72.7 * h) - 58)
mulheres = float((62.1 * h) - 44.7)
print(f"a - Para homens: {homens}")
print(f"b - Para mulheres: {mulheres}")