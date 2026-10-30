import pandas as pd

dados = {
    "Nome": ["Ana", "Bruno", "Carla", "David", "Eva", "Felipe", "Gabriela", "Hugo", "Isabela", "João"],
        "Idade": [23, 35, 29, 55, 42, 31, 27, 38, 24, 30],
        "Cidade": ["Brasília", "São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte", "Porto Alegre", "Fortaleza", "Salvador", "Recife", "Manaus",],
        "Profissão": ["Engenheiro", "Médico", "Advogado", "Professor", "Arquiteto", "Designer", "Jornalista", "Ciêntista", "Músico", "Ator"],
        "Nacionalidade": ["Brasileiro", "Chileno", "Argentino", "Peruano", "Colombiano", "Uruguaio", "Paraguáio", "Venezuelano", "Boliviano", "Equuatoriano"]
    # "Nome": ["Ana", "Bruno", "Carla"],
    # "Idade": [23, 35, 29],
    # "Cidade": ["Brasília", "São Paulo", "Rio de Janeiro"]
}

df = pd.DataFrame(dados)

# Filtrar pessoas com idade maior que 25
print(df[df["Idade"] >= 20])

# Calcular a média da coluna Idade
print(df["Idade"].mean())
