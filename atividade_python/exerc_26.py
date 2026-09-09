num1 = int(input("Digite o  primeiro numero " ))
num2 = int(input("Digite o segundo numero " ))

if num1 % 5 == 0 and num2 % 5 == 0:
    print(f"Os números {num1} e {num2} são multiplos de 5")

else:
    print(f"Pelo menos um dos números ({num1}, {num2} não são multiplos de 5)")


# Desenvolva um algoritmo que peça ao usuário para inserir dois números e verifique se ambos são múltiplos de 5.