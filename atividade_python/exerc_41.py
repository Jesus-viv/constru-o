

numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é positivo
if numero > 0:
    print("Números de 1 até", numero, ":")
    for i in range(1, numero + 1):
        print(i)
else:
    print("Número inválido! Digite um inteiro positivo.")


    #  41. Crie um programa que peça ao usuário um número inteiro positivo e exiba todos os números de 1 até o número informado.