
numero = int(input("Digite um número: "))

# Verifica se é múltiplo de 2 ou de 5
if numero % 2 == 0 and numero % 5 == 0:
    print("O número é múltiplo de 2 e de 5.")
elif numero % 2 == 0:
    print("O número é múltiplo de 2.")
elif numero % 5 == 0:
    print("O número é múltiplo de 5.")
else:
    print("O número não é múltiplo de 2 nem de 5.")


#37. Desenvolva um algoritmo que peça ao usuário para digitar um número e verifique se ele é múltiplo de 2 ou de 5.