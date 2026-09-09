

palavra = ""
while palavra.lower() != "sair":
    palavra = input("Digite uma palavra (ou 'sair' para encerrar): ")
    if palavra.lower() != "sair":
        print(f"Você digitou: {palavra}")

print("Programa encerrado.")


#58. Desenvolva um algoritmo que solicite ao usuário uma palavra e continue pedindo outra palavra até que ele digite "sair"