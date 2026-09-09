# Programa que solicita 5 números e exibe o maior e o menor

numeros = []  # lista vazia

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

print("Lista de números digitados:", numeros)
print("O maior número é:", maior)
print("O menor número é:", menor)


#65. Escreva um programa que solicite ao usuário uma lista de 5 números e exiba o maior e o menor número dessa lista.
