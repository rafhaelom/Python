# 8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

print("Informe o preço de três protudos!\n")

prod1 = float(input("Preço do primeiro produto: "))
prod2 = float(input("Preço do segundo produto: "))
prod3 = float(input("Preço do terceiro produto: "))

if(prod1 < prod2 and prod1 < prod3):
    print(f"O mais barato é: R$ {prod1}")
elif(prod2 < prod1 and prod2 < prod3):
    print(f"O mais barato é: R$ {prod2}")
elif(prod3 < prod1 and prod3 < prod2):
    print(f"O mais barato é: R$ {prod3}")
elif(prod1 == prod2 or prod1 == prod3):
    print(f"Dois são do mesmo preço e mais barato: R$ {prod1}")
elif(prod2 == prod1 or prod2 == prod3):
    print(f"Dois são do mesmo preço e mais barato: R$ {prod1}")
elif(prod3 == prod1 or prod3 == prod2):
    print(f"Dois são do mesmo preço e mais barato: R$ {prod1}")
elif(prod1 == prod2 and prod1 == prod3):
    print("Todos são do mesmo preço!")
else:
    print("Preço inválido!")