# Anotações

- Maximum à posteriori: sistema de classificação que escolherá sempre o de maior probabilidade;
- Minimum à posteriori: sistema de classificação que escolherá sempre o de menor probabilidade;
- Probabilidade: dadas as suas chances, escolhe um de acordo com um sorteio de 1 a 100, sendo esses valores associados às probabilidades.

O cálculo de probabilidade condicional é:

$$
P(C|A \wedge B) = \frac{P(C|A) * P(C|B)}{P(C)}
$$

É daí que nasce o `Naive Bayes`. Esse algoritmo calcula as probabilidades condicionais dos eventos para definir a probabilidade de um evento futuro acontecer.

A seleção de variáveis para o algoritmo pode ser interessante para identificar quais variáveis possuem maior relevância, porém testar continuamente vai resultar em uma alta correlação espúria.

Outro algoritmo a ser utilizado é o Ada Boost. Não foi explicado com maiores detalhes como funciona o Ada Boost.

Uma boa prática de machine learning é a divisão da base de dados em teste, treino e validação. Como dividir é incerto, porém uma prática comum é 80% de teste, 10% de treino e 10% para validação.
