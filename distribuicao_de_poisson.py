#Importação para fazer Distribuição de Poisson
from scipy.stats import poisson

#Média de acidentes são 2 por dia

#Qual a probabilidade de ocorrerem 3 acidentes no dia?
print(poisson.pmf(3, 2))

#Qual a probabilidade de ocorrerem 3 ou menos acidentes no dia?
print(poisson.cdf(3, 2))

#Qual a probabilidade de ocorrerem mais de 3 aciedentes no dia?
print(poisson.sf(3, 2))

