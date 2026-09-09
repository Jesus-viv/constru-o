senha_correta = "1234"

while True:
    senha = (input("Digite a senha: "))
    if senha == senha_correta:
        print("Acesso permitido")
        
    else:
        print("Senha incorreta, tente novamente.")





# 52. Desenvolva um algoritmo que solicite ao usuário uma senha e continue pedindo até que a senha correta "1234" seja digitada.

# # Programa que solicita senha com limite de 3 tentativas

# senha_correta = "1234"
# tentativas = 0
# limite = 3

# while tentativas < limite:
#     senha = input("Digite a senha: ")
#     if senha == senha_correta:
#         print("Acesso permitido!")
#         break
#     else:
#         tentativas += 1
#         print(f"Senha incorreta. Tentativa {tentativas} de {limite}.")

# if tentativas == limite and senha != senha_correta:
#     print("Acesso bloqueado! Número máximo de tentativas atingido.")
