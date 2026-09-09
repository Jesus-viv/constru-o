
def exibir_tabuleiro(tabuleiro):
    print("\n")
    for i in range(3):
        print(" | ".join(tabuleiro[i]))
        if i < 2:
            print("---------")
    print("\n")

def verificar_vencedor(tabuleiro, jogador):
    # Combina todas as possibilidades de vitória em uma lista
    linhas = tabuleiro
    colunas = [[tabuleiro[i][j] for i in range(3)] for j in range(3)]
    diagonais = [[tabuleiro[i][i] for i in range(3)], [tabuleiro[i][2-i] for i in range(3)]]

    for grupo in linhas + colunas + diagonais:
        if all(c == jogador for c in grupo):
            return True
    return False

def jogo_da_velha():
    while True:
        tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        jogador_atual = "X"
        jogadas = 0

        while True:
            exibir_tabuleiro(tabuleiro)
            print(f"Vez do jogador {jogador_atual}")

            try:
                linha = int(input("Digite a linha (0, 1 ou 2): "))
                coluna = int(input("Digite a coluna (0, 1 ou 2): "))
            except ValueError:
                print("Entrada inválida! Digite apenas números 0, 1 ou 2.")
                continue

            if linha not in [0,1,2] or coluna not in [0,1,2]:
                print("Posição inválida! Escolha entre 0, 1 ou 2.")
                continue

            if tabuleiro[linha][coluna] != " ":
                print("Posição já ocupada! Tente novamente.")
                continue

            tabuleiro[linha][coluna] = jogador_atual
            jogadas += 1

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

        # Pergunta se deseja nova partida
        resposta = input("Deseja jogar novamente? (s/n): ").lower()
        if resposta != "s":
            print("Encerrando o jogo. Obrigado por jogar!")
            break

# Executa o jogo
jogo_da_velha()



#69. Crie no algoritmo 67 as seguintes funcionalidades:
# Informe ao usuário em caso de empate.
# Crie uma forma de não permitir que um jogador jogue no mesmo lugar que já tenha uma jogada realizada.
# Atualmente o jogo encerra com o vencedor, ele agora também deve encerrar em caso de empate.
# Ao finalizar o jogo deve ser informado ao usuário uma mensagem solicitando uma nova partida, o sistema de reiniciar o jogo em caso de sim, e encerrar o programa em caso de não.
# Refatore a funcionalidade que verifica a vitoria e pense em uma forma de simplificar o código corrigido