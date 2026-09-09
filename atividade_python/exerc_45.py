maior = None


for i in range(1, 6):
    numero = int(input("Digite o numero: "))

    if maior is None or numero > maior:
        maior = numero

print("O maior numero foi: ", maior)


# 45. Escreva um algoritmo que peça ao usuário para inserir 5 números e, ao final, exiba o maior número inserido.
