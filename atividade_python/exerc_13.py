mes = int(input("Digite um mês do ano (1 a 12): "))

if mes < 1 or mes > 12:
    print("Mês inválido! Digite apenas de 1 a 12.")
elif mes in [12, 1, 2]:
    print("Estação: Verão")
elif mes in [3, 4, 5]:
    print("Estação: Outono")
elif mes in [6, 7, 8]:
    print("Estação: Inverno")
else:  # meses 9, 10, 11
    print("Estação: Primavera")



#13. Crie um algoritmo que solicite ao usuário um mês do ano (1 a 12) e exiba a estação do ano correspondente.