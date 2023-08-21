import pandas as pd

data = {
    'Nome': ['Antonio', 'Vicente', 'Clarice', 'Joao', 'Ana'],
    'Idade': [25, 30, 22, 28, 24],
    'Gênero': ['F', 'M', 'M', 'M', 'F']
}

df = pd.DataFrame(data)

coluna_idade = df['Idade']
print("Coluna 'Idade':")
print(coluna_idade)

filtro_idade = df[df['Idade'] > 25]
print("\nLinhas com idade maior que 25:")
print(filtro_idade)
