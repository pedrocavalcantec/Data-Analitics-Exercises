import pandas as pd
import numpy as np


data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, np.nan],
    'C': [1, np.nan, np.nan, 4, 5]
}

df = pd.DataFrame(data)


print("Valores ausentes:")
print(df.isna())


df_sem_nulos_linhas = df.dropna()


df_sem_nulos_colunas = df.dropna(axis=1)


df_preenchido_zero = df.fillna(0)


df_preenchido_media = df.fillna(df.mean())


df_interp = df.interpolate()


thresh_valor = 2
df_limpo = df.dropna(thresh=thresh_valor)


print("\nDataFrame sem linhas nulas:")
print(df_sem_nulos_linhas)

print("\nDataFrame sem colunas nulas:")
print(df_sem_nulos_colunas)

print("\nDataFrame preenchido com zero:")
print(df_preenchido_zero)

print("\nDataFrame preenchido com média:")
print(df_preenchido_media)

print("\nDataFrame com interpolação:")
print(df_interp)

print("\nDataFrame após remoção de linhas com mais de", thresh_valor, "valores nulos:")
print(df_limpo)