pares = []

for i in range(1 , 11):
    numero = int(input(f"Digite o {i}º número :"))
    if numero % 2 == 0:
        pares.append(numero)

print("Os numeros digitados são:", pares)

# 44. Crie um programa que peça ao usuário 10 números e exiba apenas os números pares.