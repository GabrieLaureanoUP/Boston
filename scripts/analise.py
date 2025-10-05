# Análise Exploratória de Dados - Housing Dataset
# Autor: Gabriel Laureano
# Data: 05/10/2025

# Importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Carregando o dataset
df = pd.read_csv('HousingData.csv')
df.columns = df.columns.str.strip()

"""
- CRIM: taxa de criminalidade per capita por cidade
- ZN: proporção de terrenos residenciais zoneados para lotes com mais de 25.000 pés quadrados
- INDUS: proporção de acres de negócios não varejistas por cidade
- CHAS: variável dummy do rio Charles (1 se o terreno faz fronteira com o rio; 0 caso contrário)
- NOX: concentração de óxidos nítricos (partes por 10 milhões)
- RM: número médio de quartos por habitação
- AGE: proporção de unidades ocupadas pelo proprietário construídas antes de 1940
- DIS: distâncias ponderadas até cinco centros de emprego de Boston
- RAD: índice de acessibilidade a rodovias radiais
- TAX: taxa de imposto sobre a propriedade de valor total por $10.000
- PTRATIO: proporção aluno-professor por cidade
- B: 1000(Bk - 0.63)^2 onde Bk é a proporção de negros por cidade
- LSTAT: % de população de status inferior
- MEDV: Valor mediano de residências ocupadas pelo proprietário em $1000s
"""

# ----- Análise de concentração e a distribuição das colunas numéricas  -----

# Visão geral do dataset
print("\n ##### Visão geral ##### \n")
df.info()
print("\n-----------------------------------------------")
print("##### Resumo inicial ##### \n")
print(df.describe()) # Termos valores no formato object, ta na hora da conversão, eu ouvi um amém imrãos?

# Convertendo as colunas object
colunas_para_converter = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'AGE', 'LSTAT']
for colunas in colunas_para_converter:
    df[colunas] = pd.to_numeric(df[colunas], errors='coerce') # Transforma "NA" em "NaN"

df.info()
print("\n##### Resumo inicial ##### \n")
print(df.describe())

# ----- Teste de normalidade Shapiro-Wilk -----
print("\n##### Teste de Shapiro-Wilk para normalidade #####\n")
colunas_numericas = df.select_dtypes(include=['float64', 'int64']).columns
for coluna in colunas_numericas:
    dados = df[coluna].dropna()
    stat, p = stats.shapiro(dados)
    print(f"Coluna: {coluna} | Estatística: {stat:.4f} | p-valor: {p:.4f}")
    if p > 0.05:
        print("  -> Distribuição normal")
    else:
        print("  -> Distribuição não normal")

