# Create the dataset as a pandas DataFrame
import pandas as pd

data = {
    "Estado": [
        "Alabama",
        "Alasca",
        "Arizona",
        "Arkansas",
        "Califórnia",
        "Colorado",
        "Connecticut",
        "Delaware"
    ],
    "População": [
        4779736,
        710231,
        6392017,
        2915918,
        37253956,
        5029196,
        3574097,
        897934
    ],
    "Taxa de Homicídio": [
        5.7,
        5.6,
        4.7,
        5.6,
        4.4,
        2.8,
        2.4,
        5.8
    ]
}

df = pd.DataFrame(data)

file_path = "livros-anotacoes\Estatistica-Pratica-Para-Cientistas-De-Dados\\tabela-1-2.csv"
df.to_csv(file_path, index=False)

file_path