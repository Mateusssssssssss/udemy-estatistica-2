# Importação Qui-Quadrado e numpy
import numpy as np
from scipy.stats import chi2_contingency
# Teste é baseado em quantidade de homens e mulheres que assistem e não assistem novelas
# Primero [19, 6] homens que assistem 19, que não assistem 6
# Segundo [43 , 32] mulheres que assistem 43, que não assistem 32

# Criação de array com os dados e execução dos testes
dados = np.array([[19,6], [43,32]])
print(dados)

#Segundo valor é o p-value
#Se p-value maior que 0.05 não há evidencia de diferenças significativa (hipotese nula = H0): Não há diferença significativa
p = chi2_contingency(dados)
# P maior que 0.05
print(p)


#Segundo valor é o p-value
#Se p-value menor que 0.05, podemos rejeitar a hipotese nula em favor da hipotese alternativa: Há diferença significativa
dados1 = np.array([[22,3], [43,32]])
print(dados1)

p1 = chi2_contingency(dados1)
print(p1)
