# 9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
print("Informe três números!\n")

num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))
num3 = float(input("Terceiro número: "))

if(num1 > num2 and num2 > num3):
    print(num1, ">", num2, ">", num3)
elif(num2 > num3 and num1 > num3):
    print(num2, ">", num3, ">", num1)
else:
    print(num3, ">", num2, ">", num1)