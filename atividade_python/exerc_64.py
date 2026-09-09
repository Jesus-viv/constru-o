import random

numeros = [random.randint(1, 100) for _ in range(10)]

print("Lista completa de números:", numeros)

multiplos_de_3 = [n for n in numeros if n % 3 == 0]

print("Números múltiplos de 3:", multiplos_de_3)


#64. Crie uma lista com 10 números aleatórios e exiba apenas os números que são múltiplos de 3.