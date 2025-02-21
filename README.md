# udemy estatistica 2
# Usando T-Study
# Análise de Probabilidade Salarial de Cientistas de Dados

Este repositório contém um exemplo de cálculo estatístico utilizando a distribuição t-Student para determinar a probabilidade de um cientista de dados ganhar menos ou mais de R$ 80,00 por hora.

## 📌 Contexto

Temos os seguintes dados sobre os salários dos cientistas de dados:
- **Média amostral** (μ̂): R$ 75,00/hora
- **Tamanho da amostra** (n): 9 cientistas de dados
- **Desvio padrão amostral** (s): 10
- **Valor de interesse**: R$ 80,00/hora

Nosso objetivo é calcular:
1. A probabilidade de selecionar um cientista de dados cujo salário seja **menor que R$ 80/hora**.
2. A probabilidade de selecionar um cientista de dados cujo salário seja **maior que R$ 80/hora**.
3. O somatório das duas probabilidades (deve resultar em 1, pois cobre toda a distribuição).

## 🎯 Cálculo do valor t

Para calcular o valor t, utilizamos a seguinte fórmula:

\[ t = \frac{X - \bar{X}}{s / \sqrt{n}} \]

Onde:
- \( X = 80 \) (salário de interesse)
- \( \bar{X} = 75 \) (média amostral)
- \( s = 10 \) (desvio padrão amostral)
- \( n = 9 \) (tamanho da amostra)

Substituindo os valores:

\[ t = \frac{80 - 75}{10 / \sqrt{9}} \]

\[ t = \frac{5}{10 / 3} \]

\[ t = \frac{5}{3.33} \approx 1.5 \]

Assim, temos \( t = 1.5 \) com **graus de liberdade** \( df = n - 1 = 8 \).

## 🔧 Código em Python

O código abaixo calcula as probabilidades utilizando a distribuição t-Student:

```python
# Importação para fazer o teste t-Student
from scipy.stats import t

# Probabilidade de que um cientista de dados ganhe MENOS de R$ 80/hora
prob_menor_80 = t.cdf(1.5, 8)
print(prob_menor_80)

# Probabilidade de que um cientista de dados ganhe MAIS de R$ 80/hora
prob_maior_80 = t.sf(1.5, 8)
print(prob_maior_80)

# Soma das probabilidades (deve ser 1)
print(prob_menor_80 + prob_maior_80)
```

## Explicação do Código

### `t.cdf(1.5, 8)` → Probabilidade acumulada à esquerda
A função **CDF (Cumulative Distribution Function)** retorna a probabilidade acumulada **até** o valor t = 1.5 na distribuição t-Student com 8 graus de liberdade. Ou seja, dá a probabilidade de um cientista de dados ganhar **menos que R$ 80/hora**.

### `t.sf(1.5, 8)` → Probabilidade acumulada à direita
A função **SF (Survival Function)** retorna a probabilidade complementar da CDF, ou seja, a área **após** o valor t = 1.5. Isso equivale à probabilidade de um cientista de dados ganhar **mais que R$ 80/hora**.

### Soma das probabilidades
A soma de `t.cdf(1.5, 8)` e `t.sf(1.5, 8)` deve ser **igual a 1**, pois representa toda a distribuição.




---------------------------------------------------------------------------------------------------
#Distribuição de Poisson
---------------------------------------------------------------------------------------------------



# Distribuição de Poisson

Este documento explica o conceito da **Distribuição de Poisson** e como calcular probabilidades usando a biblioteca `scipy.stats` em Python.

## O que é a Distribuição de Poisson?
A **Distribuição de Poisson** é uma distribuição de probabilidade discreta que descreve a ocorrência de eventos raros dentro de um intervalo fixo de tempo ou espaço. Ela é usada quando os eventos:

- São independentes entre si.
- Ocorrem com uma taxa média constante (lambda, λ) dentro do intervalo observado.

A fórmula da distribuição de Poisson é:

\[
P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}
\]

Onde:
- \( P(X = k) \) é a probabilidade de exatamente \( k \) eventos ocorrerem.
- \( \lambda \) é a taxa média de ocorrência dos eventos.
- \( k \) é o número de ocorrências desejadas.
- \( e \) é a base do logaritmo natural (aproximadamente 2.718).

## Explicação do Código

O seguinte código em Python usa a biblioteca `scipy.stats` para calcular probabilidades com a distribuição de Poisson:

```python
# Importação para fazer Distribuição de Poisson
from scipy.stats import poisson

# Média de acidentes são 2 por dia
lambda_ = 2

# Qual a probabilidade de ocorrerem exatamente 3 acidentes no dia?
prob_3_acidentes = poisson.pmf(3, lambda_)
print(prob_3_acidentes)

# Qual a probabilidade de ocorrerem 3 ou menos acidentes no dia?
prob_ate_3_acidentes = poisson.cdf(3, lambda_)
print(prob_ate_3_acidentes)

# Qual a probabilidade de ocorrerem mais de 3 acidentes no dia?
prob_mais_3_acidentes = poisson.sf(3, lambda_)
print(prob_mais_3_acidentes)
```

### Explicação das Funções Utilizadas

1. **`poisson.pmf(3, 2)`** → Calcula a probabilidade de exatamente 3 acidentes ocorrerem em um dia.
   - `pmf` (**Probability Mass Function**) fornece a probabilidade exata de um evento ocorrer.

2. **`poisson.cdf(3, 2)`** → Calcula a probabilidade de ocorrerem **3 ou menos** acidentes no dia.
   - `cdf` (**Cumulative Distribution Function**) soma as probabilidades de 0 até 3 acidentes.

3. **`poisson.sf(3, 2)`** → Calcula a probabilidade de ocorrerem **mais de 3** acidentes no dia.
   - `sf` (**Survival Function**) é o complemento da `cdf`, ou seja, **1 - P(X ≤ 3)**.

## Interpretação dos Resultados

Se a saída do programa for algo como:

```
0.1804  # Probabilidade de exatamente 3 acidentes
0.8571  # Probabilidade de até 3 acidentes
0.1429  # Probabilidade de mais de 3 acidentes
```

Podemos interpretar que:
- Há aproximadamente **18,04%** de chance de exatamente **3 acidentes** ocorrerem no dia.
- Há aproximadamente **85,71%** de chance de ocorrerem **3 ou menos acidentes**.
- Há aproximadamente **14,29%** de chance de ocorrerem **mais de 3 acidentes**.

## Aplicabilidade
A distribuição de Poisson é amplamente utilizada em situações reais, como:
- Número de ligações recebidas por um call center por minuto.
- Número de falhas em uma máquina por semana.
- Número de pacientes chegando a um pronto-socorro por hora.
- Número de acessos a um site por minuto.

## Conclusão
A distribuição de Poisson é uma ferramenta estatística poderosa para modelar eventos raros e pode ser usada para tomar decisões em diversas áreas como gestão, tecnologia e saúde. Este código em Python facilita a análise probabilística de tais eventos.





---------------------------------------------------------------------------------------------------
##Distribuição Binomial e Probabilidades
---------------------------------------------------------------------------------------------------

# Distribuição Binomial e Probabilidades

Este documento explica os conceitos por trás da distribuição binomial e fornece um exemplo de implementação em Python utilizando a biblioteca `scipy.stats`.

## Conceitos
A **Distribuição Binomial** é um modelo probabilístico discreto usado para calcular a probabilidade de um determinado número de sucessos em um conjunto fixo de tentativas independentes, onde cada tentativa tem apenas dois resultados possíveis: sucesso ou fracasso.

A fórmula para a probabilidade binomial é:

\[ P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k} \]

Onde:
- \( n \) = número total de tentativas (ou ensaios)
- \( k \) = número de sucessos desejado
- \( p \) = probabilidade de sucesso em cada tentativa
- \( \binom{n}{k} \) = coeficiente binomial, que representa as diferentes maneiras de escolher \( k \) sucessos em \( n \) tentativas

## Implementação em Python

O seguinte código ilustra a aplicação da distribuição binomial para diferentes cenários:

```python
from scipy.stats import binom

# Jogar a moeda 5 vezes - qual a probabilidade de cair cara 3 vezes?
prob = binom.pmf(3, 5, 0.5)
print(prob)

# Passar por 4 sinais de 4 tempos, qual a probabilidade de pegar sinal verde?
# Nenhum, 1, 2, 3 ou 4 vezes seguidas
temp = binom.pmf(0, 4, 0.25)
temp1 = binom.pmf(1, 4, 0.25)
temp2 = binom.pmf(2, 4, 0.25)  
temp3 = binom.pmf(3, 4, 0.25)
temp4 = binom.pmf(4, 4, 0.25)
print(f'Probabilidade de:
 - Nenhum sinal verde: {temp}\n - Um sinal verde: {temp1}\n - Dois sinais verdes: {temp2}\n - Três sinais verdes: {temp3}\n - Quatro sinais verdes: {temp4}')

# Se forem sinais de 2 tempos
sinal_2temp = binom.pmf(4, 4, 0.5)
print(sinal_2temp)

# Probabilidade acumulativa
prob_acumulativa = binom.cdf(4, 4, 0.25)
print(f'Probabilidade acumulativa: {prob_acumulativa}')

# Concurso com 12 questões, qual a probabilidade de acertar 7 considerando 4 alternativas por questão?
questao = binom.pmf(7, 12, 0.25)
print(questao)
```

## Explicação dos Cálculos

1. **Jogar uma moeda 5 vezes**: A probabilidade de obter exatamente 3 caras em 5 lançamentos, considerando que a chance de cara em cada lançamento é 50%.
2. **Passar por 4 sinais de 4 tempos**: Calculamos a probabilidade de pegar de 0 a 4 sinais verdes, considerando que a probabilidade de pegar um sinal verde é 25%.
3. **Sinais de 2 tempos**: Se a probabilidade de pegar um sinal verde aumenta para 50%, a chance de pegar 4 sinais verdes seguidos muda.
4. **Probabilidade acumulativa**: Probabilidade de pegar até 4 sinais verdes.
5. **Concurso com 12 questões**: Probabilidade de acertar exatamente 7 questões quando cada uma tem 4 alternativas (portanto, 25% de chance de acerto por questão).

## Conclusão
A distribuição binomial é muito útil para modelar situações onde temos um número fixo de tentativas independentes com dois resultados possíveis. Utilizamos `binom.pmf` para calcular a probabilidade de um valor específico e `binom.cdf` para calcular a probabilidade acumulativa.

Este código fornece um exemplo prático de como podemos aplicar esses conceitos para responder a perguntas do dia a dia.




 
