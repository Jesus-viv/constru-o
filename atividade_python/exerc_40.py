# Programa que verifica se três números são iguais

# Solicita os números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Verifica se todos são iguais
if num1 == num2 == num3:
    print("Todos os números são iguais.")
else:
    print("Os números não são todos iguais.")
