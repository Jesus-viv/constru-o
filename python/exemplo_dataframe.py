import pandas as pd

dados = {
    "Nome": ["Ana", "Bruno", "Carla", "David", "Eva", "Felipe", "Gabriela", "Hugo", "Isabela", "João"],
    "Idade": [23, 35, 29, 55, 42, 31, 27, 38, 24, 30],
    "Cidade": ["Brasília", "São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte", "Porto Alegre", "Fortaleza", "Salvador", "Recife", "Manaus",],
}

df = pd.DataFrame(dados)
print(df)
