cadastrados = []

def cadastrar_nome():
    nome = input("Digite o nome a ser cadastrado: ")
    cadastrados.append(nome)
    print(f'Nome "{nome}" cadastrado com sucesso!')

def atualizar_nome():
    if not cadastrados:
        print("Não há nomes cadastrados para atualizar.")
        return
    listar_nomes()
    try:
        indice = int(input("Digite o número do nome que deseja atualizar: ")) - 1
        if 0 <= indice < len(cadastrados):
            nome_antigo = cadastrados[indice]
            novo_nome = input("Digite o novo nome: ")
            cadastrados[indice] = novo_nome
            print(f'Nome "{nome_antigo}" atualizado para "{novo_nome}" com sucesso!')
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

def excluir_nome():
    if not cadastrados:
        print("Não há nomes cadastrados para excluir.")
        return
    listar_nomes()
    try:
        indice = int(input("Digite o número do nome que deseja excluir: ")) - 1
        if 0 <= indice < len(cadastrados):
            nome_removido = cadastrados.pop(indice)
            print(f'Nome "{nome_removido}" excluído com sucesso!')
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

def listar_nomes():
    if not cadastrados:
        print("Não há nomes cadastrados.")
    else:
        print("--- Lista de cadastrados ---")
        for i, nome in enumerate(cadastrados, start=1):
            print(f"{i} - {nome}")
        print("----------------------------")

def exibir_menu():
    print("\n===== MENU =====")
    print("1 - Cadastrar nome")
    print("2 - Atualizar nome")
    print("3 - Excluir nome")
    print("4 - Listar todos os cadastrados")

continuar = True

while continuar:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_nome()
    elif opcao == "2":
        atualizar_nome()
    elif opcao == "3":
        excluir_nome()
    elif opcao == "4":
        listar_nomes()
    else:
        print("Opção inválida!")

    resposta = input("Deseja realizar outra operação? (s/n): ").strip().lower()
    if resposta != "s":
        continuar = False
        print("Aplicativo encerrado. Até logo!")



    #66 Escreva um algoritmo que forneça um menu para o usuário: 1-Cadastrar nome, 2- atualizar o nome, 3, excluir, 4-listar todos os cadastrados, ao final da operação deve dar uma mensagem indicando o resultado da operação e perguntando se deseja realizar outra operação, o seu aplicativo apenas deve encerrar quando a opção não for inserida