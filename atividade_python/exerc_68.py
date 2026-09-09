import uuid
import re

# ------------------ Módulo de Validações ------------------
def validar_nome(nome):
    return len(nome.strip()) > 0

def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email) is not None

def validar_data_nascimento(data):
    padrao = r'^\d{2}/\d{2}/\d{4}$'  # formato DD/MM/AAAA
    return re.match(padrao, data) is not None

# ------------------ Módulo de Alunos ------------------
class Aluno:
    def __init__(self, nome, email, data_nascimento):
        if not validar_nome(nome):
            raise ValueError("Nome inválido.")
        if not validar_email(email):
            raise ValueError("E-mail inválido.")
        if not validar_data_nascimento(data_nascimento):
            raise ValueError("Data de nascimento inválida. Use DD/MM/AAAA.")

        self.nome = nome
        self.email = email
        self.data_nascimento = data_nascimento
        self.matricula = str(uuid.uuid4())[:8]  # gera matrícula única

    def __str__(self):
        return (f"Matricula: {self.matricula}\n"
                f"Nome: {self.nome}\n"
                f"E-mail: {self.email}\n"
                f"Data de Nascimento: {self.data_nascimento}\n")

# ------------------ Módulo de Sistema ------------------
class SistemaCadastro:
    def __init__(self):
        self.alunos = {}

    def cadastrar_aluno(self, nome, email, data_nascimento):
        try:
            aluno = Aluno(nome, email, data_nascimento)
            self.alunos[aluno.matricula] = aluno
            print("Aluno cadastrado com sucesso!")
            print(aluno)
        except ValueError as e:
            print("Erro ao cadastrar aluno:", e)

    def atualizar_aluno(self, matricula, campo, novo_valor):
        aluno = self.alunos.get(matricula)
        if not aluno:
            print("Matrícula inválida.")
            return

        try:
            if campo == "nome" and validar_nome(novo_valor):
                aluno.nome = novo_valor
            elif campo == "email" and validar_email(novo_valor):
                aluno.email = novo_valor
            elif campo == "data_nascimento" and validar_data_nascimento(novo_valor):
                aluno.data_nascimento = novo_valor
            else:
                print("Valor inválido para atualização.")
                return
            print("Dados atualizados com sucesso!")
        except Exception as e:
            print("Erro ao atualizar:", e)

    def remover_aluno(self, matricula):
        if matricula in self.alunos:
            del self.alunos[matricula]
            print("Aluno removido com sucesso.")
        else:
            print("Matrícula inválida.")

    def listar_alunos(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
        else:
            for aluno in self.alunos.values():
                print(aluno)
                print("-" * 30)

    def mostrar_aluno(self, matricula):
        aluno = self.alunos.get(matricula)
        if aluno:
            print(aluno)
        else:
            print("Matrícula inválida.")

# ------------------ Programa Principal ------------------
if __name__ == "__main__":
    sistema = SistemaCadastro()

    while True:
        print("\n--- MENU ---")
        print("1. Cadastrar aluno")
        print("2. Atualizar aluno")
        print("3. Remover aluno")
        print("4. Listar todos os alunos")
        print("5. Mostrar aluno específico")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("E-mail: ")
            data = input("Data de nascimento (DD/MM/AAAA): ")
            sistema.cadastrar_aluno(nome, email, data)
        elif opcao == "2":
            matricula = input("Digite a matrícula: ")
            campo = input("Campo para atualizar (nome/email/data_nascimento): ")
            novo_valor = input("Novo valor: ")
            sistema.atualizar_aluno(matricula, campo, novo_valor)
        elif opcao == "3":
            matricula = input("Digite a matrícula: ")
            sistema.remover_aluno(matricula)
        elif opcao == "4":
            sistema.listar_alunos()
        elif opcao == "5":
            matricula = input("Digite a matrícula: ")
            sistema.mostrar_aluno(matricula)
        elif opcao == "6":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida.")



# # 68. Crie uma nova versão do algoritmo 66, aplicando o conceito de módulos e dividindo as responsabilidades, receberemos agora não somente o nome, mas simularemos um sistema de cadastro de alunos, esta nova versão deve atender as novas funcionalidade a seguir:
# Cada aluno cadastrado deve ter atrelado a seus dados pessoais (nome, e-mail, data de nascimento, matricula), no caso de matricula você deve gerar uma matricula unica para cada aluno cadastrado.
# Cada um dos dados do aluno devem ser validade de forma o código não quebre ao serem informados valores incorretos.
# Para atualizar qualquer dado do aluno você deve localiza-lo utilizando de sua matricula para isso. Valide de forma que o sistema não quebre ao ser inserido uma matricula invalida.
# Para remover um aluno deve-se realizar esta ação usando de sua matricula, o sistema não pode quebrar ao ser inserido uma matricula errada.
# Ao listar todos os alunos mostre cada um de forma organizada e separada.
# Crie uma funcionalidade de mostre os dados de um aluno especifico usando apenas de sua matricula para isso.