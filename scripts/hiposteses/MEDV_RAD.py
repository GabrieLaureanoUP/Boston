## HIPOTESE 2 - MEDV X RAD
# Imóveis localizados em áreas com maior acesso a rodovias (RAD) tendem a ter menor valor de mercado (MEDV).

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr   

df = pd.read_csv('HousingData.csv')
df.columns = df.columns.str.strip()

corr_pearson, p_value = pearsonr(df['RAD'], df['MEDV'])

# Classificação da direção
direcao = 'positiva' if corr_pearson > 0 else 'negativa'

# Classificação da força
if abs(corr_pearson) > 0.7:
    forca = 'forte'
elif abs(corr_pearson) > 0.3:
    forca = 'moderada'
else:
    forca = 'fraca'

# Análise completa da correlação
print(f"\n=== ANÁLISE DE CORRELAÇÃO: RAD vs MEDV ===")
print(f"VALOR: r = {corr_pearson:.4f}")
print(f"DIREÇÃO: {direcao.capitalize()}")
print(f"FORÇA: {forca.capitalize()}")
print(f"INTERPRETAÇÃO: Correlação {direcao} {forca} entre acesso a rodovias e valor dos imóveis")
print(f"="*60)

# Visualização
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.scatter(df['RAD'], df['MEDV'], alpha=0.7)
plt.xlabel('Acesso a Rodovias (RAD)')
plt.ylabel('Valor dos Imóveis (MEDV)')
plt.title(f'Correlação: r = {corr_pearson:.3f}')

plt.subplot(1, 2, 2)
sns.regplot(x='RAD', y='MEDV', data=df, ci=None)
plt.title('Reta de Regressão')

plt.tight_layout()
plt.show()

# Teste de hipótese detalhado
alpha = 0.05
print(f"\n=== TESTE DE HIPÓTESE DA CORRELAÇÃO ===")
print(f"H₀: ρ = 0 (Não há correlação linear entre RAD e MEDV)")
print(f"H₁: ρ ≠ 0 (Há correlação linear entre RAD e MEDV)")
print(f"Nível de significância: α = {alpha}")
print(f"Estatística do teste: r = {corr_pearson:.4f}")
print(f"Valor-p: {p_value:.2e}")  # Notação científica
print(f"Valor-p (6 decimais): {p_value:.6f}")

if p_value < alpha:
    print(f"DECISÃO: Como p-valor ({p_value:.6f}) < α ({alpha}), rejeitamos H₀")
    print(f"CONCLUSÃO: Há evidências estatisticamente significativas de correlação {direcao} {forca} entre RAD e MEDV")
else:
    print(f"DECISÃO: Como p-valor ({p_value:.6f}) ≥ α ({alpha}), não rejeitamos H₀")
    print(f"CONCLUSÃO: Não há evidências estatisticamente significativas de correlação linear entre RAD e MEDV")