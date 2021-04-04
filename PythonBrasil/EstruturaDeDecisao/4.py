# 4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Digite uma letra: ").lower())
vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['B', 'C', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']

if(letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
    print(f"A letra [{letra}] é uma Vogal")
elif(letra == 'h'):
    print(f"A letra [{letra}] não é nem consoante e nem vogal por não possuir som ou ruído e por isso, se torna a única letra diacrítica.")
else:
    print(f"A letra [{letra}] é uma Consoante")