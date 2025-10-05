# Análise de Corelação em Pares - Heatmap e Estatísticas de correlação forte e moderada
# Autor: Gabriel Laureano
# Data: 05/10/2025

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

df = pd.read_csv('HousingData.csv')
correlation_matrix = df.corr()

plt.figure(figsize=(12,10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Heatmap de Correlação entre Variáveis Numéricas')
plt.show()

strong_corrs = correlation_matrix[(correlation_matrix > 0.5) | (correlation_matrix < -0.5)]

# Lista para armazenar os resultados
resultados = []

# Lista de colunas numéricas
colunas = df.select_dtypes(include='number').columns

# Loop por todos os pares únicos
for i in range(len(colunas)):
    for j in range(i+1, len(colunas)):
        var1 = colunas[i]
        var2 = colunas[j]
        corr, p = pearsonr(df[var1], df[var2])
        if abs(corr) >= 0.3:
            direcao = 'Positiva' if corr > 0 else 'Negativa'
            if (abs(corr) > 0.7 and abs(corr) < 1):
                força = 'Forte'
            else:
                força = 'Moderada'
            significancia = 'Significativa' if p < 0.05 else 'Não significativa'
            print(f"r({var1}, {var2}) = {corr:.4f}")
            resultados.append({
                'Variável 1': var1,
                'Variável 2': var2,
                'Correlação': round(corr, 2),
                'Direção': direcao,
                'Força': força,
                'p-valor': round(p, 4),
                'Significância': significancia
            })

# Criar DataFrame com os resultados
df_resultados = pd.DataFrame(resultados)
print(df_resultados.sort_values(by='Correlação', key=abs, ascending=False))

