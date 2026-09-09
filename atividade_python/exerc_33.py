valor = float(input("Digite o valor do produto: R$ "))

# Calcula o desconto de 10%
desconto = valor * 0.10
valor_final = valor - desconto

# Exibe os resultados
print("Desconto aplicado: R$ {:.2f}".format(desconto))
print("Valor com desconto: R$ {:.2f}".format(valor_final))

#33. Crie um programa que solicite ao usuário o valor de um produto e calcule o desconto de 10%