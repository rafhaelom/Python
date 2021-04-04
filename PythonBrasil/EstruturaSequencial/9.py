# Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

temFahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
print("A temperatura em Celsius eh: ", 5 * ((temFahrenheit - 32) / 9), "ºC")