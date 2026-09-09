dias = {
    1: "Segunda-Feira",
    2: "Terça-Feira",
    3: "Quarta-Feira",
    4: "Quinta-Feira",
    5: "Sexta-Feira",
    6: "Sábado",
    7: "Domingo",
    8: "Segunda-Feira",
    9: "Terça-Feira",
    10: "Quarta-Feira",
    11: "Quinta-Feira",
    12: "Sexta-Feira",
    13: "Sábado",
    14: "Domingo"
}

numero = int(input("Digite um número de 1 a 14: "))

if numero in dias:
    print(f"O dia equivalente é: {dias[numero]}")
else:
    print("Número inválido! Digite apenas de 1 a 14.")


#3. Desenvolva um programa que pergunte ao usuário o dia da semana (número de 1 a 7) e exiba o nome do dia correspondente.