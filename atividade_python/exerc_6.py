operacao = input("Digite a operação (+, -, *, /): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operacao == "+":
    resultado = num1 + num2
    print(f"O Resultado é :{resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"O Resultado é: {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"O Resultado é: {resultado}")
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {resultado}")
    else:
        print("Erro: divisão por zero não é permitida.")
else:
    print("Operação inválida! Digite apenas +, -, * ou /.")


#6. Desenvolva um programa que pergunte ao usuário uma operação matemática (+, -, *, /) e dois números, e realize a operação escolhida.

#Dentro do caso da divisão (/), é necessário fazer uma verificação extra: se o divisor (num2) é diferente de zero.

# Isso evita um erro de execução, já que divisão por zero não é permitida em Python.

# Ou seja, o segundo if é uma condição especial que só faz sentido dentro do contexto da divisão.

#  Em resumo:

# O primeiro nível de if/elif decide qual operação executar.

# O segundo nível de if trata uma condição específica daquela operação (no caso, evitar erro de divisão por zero).