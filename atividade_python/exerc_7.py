nota = float(input("Digite uma nota de 0 a 10: "))

if nota < 0 or nota > 10:
    print("Nota inválida! Digite apenas entre 0 e 10.")
elif nota <= 6.9:
    print("Classificação:  Nota Baixa")
elif nota <= 7:
    print("Classificação:  Média")
else:
    print("Classificação: Alta")



#7. Escreva um programa que peça ao usuário uma nota de 0 a 10 e classifique a nota como "Baixa", "Média" ou "Alta" usando estrutura condicional if.