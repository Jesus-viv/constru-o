combustivel = input("Digite o tipo de combistivel(gasolina, alcool, diesel)")

if combustivel == "gasolina":
    print(f"O preço da gasolina por litro é: R$ 5,80")

elif combustivel == "alcool":
    print(f"O preço do alcool por litro é R$ 4,68")

elif combustivel == "diesel":
    print(f"O preço do diesel por litro é R$ 6,95")

else:
    print("Combustível inválido! Por gentileza escolha apenas (gasolina, alcool, diesel) ")


    #16. Desenvolva um programa que peça ao usuário um tipo de combustível (gasolina, etanol, diesel) e exiba o preço correspondente por litro.