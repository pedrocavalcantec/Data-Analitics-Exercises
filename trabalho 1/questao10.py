import pandas as pd
import numpy as np


data = {
    'Pontuação': [80, 85, 90, 88, 92, 95, 97, 100, 105, 110, 120]
}

df = pd.DataFrame(data)

print("DataFrame original:")
print(df)

z_scores = np.abs((df - df.mean()) / df.std())

limiar = 2

df_sem_outliers = df[(z_scores <= limiar).all(axis=1)]

print("\nDataFrame após a remoção de outliers:")
print(df_sem_outliers)
