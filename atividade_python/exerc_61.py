
numero = int(input("Digite um número: "))

print(f"Os divisores de {numero} são:")
divisor = 1
while divisor <= numero:
    if numero % divisor == 0:
        print(divisor)
    divisor += 1



#61. Crie uma lista contendo os números de 1 a 5 e imprima cada número da lista em uma linha separada.