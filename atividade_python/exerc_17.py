num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

if num2 != 0:
    divisao = num1 / num2
    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Divisão: {divisao}")
else:
    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print("Divisão: Erro - divisão por zero não é permitida.")


#17. Crie um programa que solicite ao usuário dois números e exiba a soma, subtração, multiplicação e divisão entre eles.