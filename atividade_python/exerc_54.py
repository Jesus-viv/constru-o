while True:
    numero = float(input("Digite um numero negativo para parar o loop: "))
    if numero < 0:
        print("Programa encerrado! Você digitou um numero negativo: ")
        break
    else:
        print(f"Você digitou :{numero}")



# 54. Crie um algoritmo que solicite ao usuário um número e continue pedindo outro número até que um número negativo seja inserido.