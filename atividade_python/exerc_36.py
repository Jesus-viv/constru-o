numero = int(input("Digite o numero de 1 a 12: "))

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio","Junho", "Julho", "Agosto", "Setembro",
         "Outubro", "Novembro", "Dezembro"]

if 1 <= numero <= 12:
    print("O mês correspondênte é :", meses[numero - 1])
else:
    print("Numero inválido! Digite um valor entre 1 a 12.")


#36. Crie um programa que solicite ao usuário um número de 1 a 12 e exiba o mês correspondente.
