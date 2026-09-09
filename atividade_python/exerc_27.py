# Programa que solicita três números e exibe o maior deles

# Solicita os números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Determina o maior número
maior = max(num1, num2, num3)

# Exibe o resultado
print("O maior número é:", maior)
