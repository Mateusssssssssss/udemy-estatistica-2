from urllib.request import proxy_bypass
from scipy.stats import binom

#jogar a moeda 5 vezes qual a probabilidade de cair cara 3 vezes?

prob = binom.pmf(3, 5, 0.5)
print(prob)

#Passar por 4 sinais de 4 tempos, qual a probabilidade de pegar sinal verde?
#nenhum, 1, 2, 3 ou 4 vezes seguidas
temp = binom.pmf(0, 4, 0.25) 
temp1 = binom.pmf(1, 4, 0.25) 
temp2 = binom.pmf(2, 4, 0.25)  
temp3 = binom.pmf(3, 4, 0.25) 
temp4 = binom.pmf(4, 4, 0.25)
print(f'Probabilidade de não pegar nenhum sinal verde: {temp}\nUm sinal verde: {temp1}\nDois sinais verdes: {temp2}\nTres sinais verdes: {temp3}\nQuatro sinais verdes: {temp4}')
#Se forem sinais de 2 tempos
sinal_2temp = binom.pmf(4,4,0.5)
print(sinal_2temp)

#Probabilidade acumulativa 
prob_acumulativa = binom.cdf(4, 4, 0.25)
print(f'probabilidade acumulativa: {prob_acumulativa}')


#Concurso com 12 questões, qual a probabilidade  de acertar 7 questões considerando
#que cada questão tem 4 alternativas
questao = binom.pmf(7, 12, 0.25)
print(questao)