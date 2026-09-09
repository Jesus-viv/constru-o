import random

numero_secreto = random.randint(1, 10)

print("Tente adivinhar o número secreto entre 1 e 10!")

palpite = 0
while palpite != numero_secreto:
    palpite = int(input("Digite seu palpite: "))

print("Parabéns! Você acertou o número secreto!")
