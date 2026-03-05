import pandas as pd
import openpyxl

path = "C:/Users/pedro-admin/Desktop/ciencia-de-dados-furb/Primeiro-Semestre/Estatistica/Estatistica_-BCD-/Dados_CalourosBCD.xlsx"
df = pd.read_excel(path)
print(df.head(100))