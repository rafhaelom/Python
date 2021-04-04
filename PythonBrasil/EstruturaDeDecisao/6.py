# 6 - Faça um Programa que leia três números e mostre o maior deles.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if(num1 > num2 and num1 > num3):
    print("O maior é: %d" %num1)
elif(num2 > num1 and num2 > num3):
    print("O maior é: %d" %num2)
elif(num3 > num1 and num3 > num2):
    print("O maior é: %d" %num3)
else:
    print("Todos os números são iguais!")