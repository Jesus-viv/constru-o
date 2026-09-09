# Jogo da Velha em Python (terminal)

def exibir_tabuleiro(tabuleiro):
    print("\n")
    for i in range(3):
        print(" | ".join(tabuleiro[i]))
        if i < 2:
            print("---------")
    print("\n")

def verificar_vencedor(tabuleiro, jogador):
    # Verifica linhas
    for linha in tabuleiro:
        if all(c == jogador for c in linha):
            return True
    # Verifica colunas
    for col in range(3):
        if all(tabuleiro[linha][col] == jogador for linha in range(3)):
            return True
    # Verifica diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True
    if all(tabuleiro[i][2-i] == jogador for i in range(3)):
        return True
    return False

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogadas = 0

    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}")
        
        linha = int(input("Digite a linha (0, 1 ou 2): "))
        coluna = int(input("Digite a coluna (0, 1 ou 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
            jogadas += 1
        else:
            print("Posição já ocupada! Tente novamente.")
            continue

        if verificar_vencedor(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break

        if jogadas == 9:
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        # Alterna jogador
        jogador_atual = "O" if jogador_atual == "X" else "X"

# Executa o jogo
jogo_da_velha()



#67. desenvolva um jogo da velha em python que funcione no terminal
