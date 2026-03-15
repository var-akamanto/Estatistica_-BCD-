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