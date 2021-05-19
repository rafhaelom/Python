# 7 - Faça um Programa que leia três números e mostre o maior e o menor deles.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if(num1 > num2 and num1 > num3):
    print("O maior é: %d" %num1)
    if(num2 > num3):
        print("O menor é: %d" %num3)
    else:
        print("O menor é: %d" %num2)
elif(num2 > num1 and num2 > num3):
    print("O maior é: %d" %num2)
    if(num1 > num3):
        print("O menor é: %d" %num3)
    else:
        print("O menor é: %d" %num1)
elif(num3 > num1 and num3 > num2):
    print("O maior é: %d" %num3)
    if(num1 > num2):
        print("O menor é: %d" %num2)
    else:
        print("O menor é: %d" %num1)
else:
    print("Todos os números são iguais!")