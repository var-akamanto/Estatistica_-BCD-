""""disciplina = 'Estatistica'
quantidade_alunos = 49
quantidade_aprovados = 37
media_geral = 7.5

taxa_aprovacao = (quantidade_aprovados / quantidade_alunos)
print(f'Taxa de aprovação em {disciplina}: {taxa_aprovacao:.2%}')



media = 6
n1 = 2.5
n2 = 4.2
nota_necessaria = media * 3 - n1 - n2
print(f'{nota_necessaria:.2f}')
from numpy import mean
lista = [2.5,4.2,3.76]
print(mean(lista))"""



""" preco_final = 100
preco_original = preco_final / 1.4
print(preco_original) """


import pandas as pd
import numpy as np

alunos_notas = {
    'Alice': {'nota1': 8.5, 'nota2': 9.0, 'nota3': 7.5},
    'Bob': {'nota1': 6.0, 'nota2': 7.2, 'nota3': 8.1},
    'Charlie': {'nota1': 9.5, 'nota2': 8.8, 'nota3': 9.2},
    'Diana': {'nota1': 7.3, 'nota2': 6.9, 'nota3': 8.0},
    'Eve': {'nota1': 8.2, 'nota2': 9.1, 'nota3': 7.8}
}

df = pd.DataFrame(alunos_notas)
df["Media"] = np.sum(df[""])