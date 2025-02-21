#Importação para fazer o teste T-Study
from scipy.stats import t

# Média de  salario dos cientistas de dados = R$ 75,00 por hora, amostra de 9 funcionarios e
#desvio padrao = 10

# Qual a probabilidade de selecionar um cientista de dados e o salario ser menor 
# que R$ 80 por hora

# Usa-se cdf para a esquerda da distribuição
print(t.cdf(1.5, 8))

# Qual a probabilidade do salario ser maior que 80?

#Usa-se sf para a direita da distribuição
print(t.sf(1.5, 8))

#somatorio de ambos os lados
print(t.cdf(1.5, 8) + t.sf(1.5, 8))
