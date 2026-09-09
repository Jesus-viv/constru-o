soma = 0

while True:
    numero = float(input("Digite um número (0 para encerrar): "))
    if numero == 0:
        break
    soma += numero

print("A soma dos números digitados é:", soma)


#51. Crie um programa que peça ao usuário para inserir números até que ele digite o número 0. Ao final, exiba a soma de todos os números inseridos (exceto o 0).