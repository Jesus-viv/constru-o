
numero = int(input("Digite um número: "))

print(f"Os divisores de {numero} são:")
divisor = 1
while divisor <= numero:
    if numero % divisor == 0:
        print(divisor)
    divisor += 1


#60. Crie um programa que peça ao usuário um número e exiba todos os divisores desse número. 
