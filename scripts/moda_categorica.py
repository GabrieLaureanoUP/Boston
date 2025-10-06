# Análise da Moda das colunas categoricas - Housing Dataset
# Autor: Gabriel Laureano
# Data: 05/10/2025

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
df = pd.read_csv('HousingData.csv')
df.columns = df.columns.str.strip()

# Tratar CHAS como categórica
df['CHAS'] = df['CHAS'].astype('category')

# 1. Identificar colunas categóricas
colunas_categoricas = df.select_dtypes(include='category').columns
print(f"Colunas categóricas: {list(colunas_categoricas)}\n")

# 2. Moda e frequências da CHAS
moda_chas = df['CHAS'].mode()[0]
frequencias_chas = df['CHAS'].value_counts()
proporcao_chas = df['CHAS'].value_counts(normalize=True)
print("Moda da variável CHAS:", moda_chas)
print("Frequências:")
print(frequencias_chas)
print("Proporção:")
print(proporcao_chas)
print()

# 3. Visualizar distribuição
plt.figure(figsize=(6,4))
sns.countplot(x='CHAS', data=df)
plt.title('Distribuição da variável CHAS')
plt.show()

# 4. Relacionar CHAS com MEDV
plt.figure(figsize=(7,5))
sns.boxplot(x='CHAS', y='MEDV', data=df)
plt.title('Valor médio dos imóveis (MEDV) por proximidade ao rio Charles')
plt.show()

print("\nInterpretação:")
print(f"A variável CHAS é categórica e indica a proximidade ao rio Charles.")
print(f"A moda da variável é {moda_chas} (não próxima ao rio) e representa {proporcao_chas[moda_chas]*100:.1f}% das observações.")
if proporcao_chas[moda_chas] > 0.8:
    print("O gráfico de barras mostra um grande desequilíbrio entre as categorias.")
else:
    print("O gráfico de barras mostra equilíbrio entre as categorias.")
print("O boxplot de MEDV em relação a CHAS indica que casas próximas ao rio (CHAS=1) possuem, em média, valores mais altos, sugerindo influência positiva dessa variável sobre o preço dos imóveis.")
