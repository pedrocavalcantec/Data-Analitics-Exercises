import pandas as pd


data = {
    'Nome': ['Amanda', 'Pepe', 'Pedro'],
    'Idade': [25, 30, 22],
    'Gênero': ['F', 'M', 'M']
}

df = pd.DataFrame(data)

print("DataFrame original:")
print(df)

df_sem_genero = df.drop('Gênero', axis=1)

print("\nDataFrame após a remoção da coluna 'Gênero':")
print(df_sem_genero)