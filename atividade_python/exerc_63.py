
numeros = []  # lista vazia

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

soma = sum(numeros)

print("Lista de números digitados:", numeros)
print("A soma de todos os números é:", soma)


#63. Desenvolva um algoritmo que peça ao usuário para inserir 5 números, adicione-os a uma lista e, depois, exiba a soma de todos os números na lista.