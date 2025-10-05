import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Carregar o dataset
df = pd.read_csv('HousingData.csv')
df.columns = df.columns.str.strip()

# Selecionar colunas numéricas
colunas_numericas = df.select_dtypes(include=['float64', 'int64']).columns

print("\n===== Medidas de tendência central e dispersão =====\n")
for coluna in colunas_numericas:
    print(f"Coluna: {coluna}")
    media = df[coluna].mean()
    mediana = df[coluna].median()
    moda = df[coluna].mode()
    std = df[coluna].std()
    var = df[coluna].var()
    minimo = df[coluna].min()
    maximo = df[coluna].max()
    amplitude = maximo - minimo
    coef_var = std / media if media != 0 else float('nan')
    print(f"  Média: {media:.4f}")
    print(f"  Mediana: {mediana:.4f}")
    if not moda.empty:
        print(f"  Moda: {moda.iloc[0]:.4f}")
    else:
        print("  Moda: Não existe")
    print(f"  Desvio padrão: {std:.4f}")
    print(f"  Variância: {var:.4f}")
    print(f"  Amplitude: {amplitude:.4f}")
    print(f"  Coeficiente de variação: {coef_var:.4f}")
    print(f"  Mínimo: {minimo:.4f}")
    print(f"  Máximo: {maximo:.4f}")
    print(f"  Quartis:")
    print(df[coluna].quantile([0.25, 0.5, 0.75]))
    print()

num_cols = len(colunas_numericas)
num_cols_subplot = 7
num_rows_subplot = (num_cols // num_cols_subplot) + (1 if num_cols % num_cols_subplot != 0 else 0)

# Boxplots para cada coluna numérica
fig, axs = plt.subplots(ncols=num_cols_subplot, nrows=num_rows_subplot, figsize=(3*num_cols_subplot, 5*num_rows_subplot))
axs = axs.flatten()
for index, coluna in enumerate(colunas_numericas):
    sns.boxplot(y=coluna, data=df, ax=axs[index])
    axs[index].set_title(f'Boxplot - {coluna}')
plt.tight_layout()
plt.show()
plt.close()

# Histogramas/densidade para cada coluna numérica
fig, axs = plt.subplots(ncols=num_cols_subplot, nrows=num_rows_subplot, figsize=(3*num_cols_subplot, 5*num_rows_subplot))
axs = axs.flatten()
for index, coluna in enumerate(colunas_numericas):
    sns.histplot(df[coluna].dropna(), kde=True, ax=axs[index])
    axs[index].set_title(f'Distribuição - {coluna}')
plt.tight_layout()
plt.show()
plt.close()
