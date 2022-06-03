import pandas as pd
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier

def fit_and_predict(modelo, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes):
    modelo.fit(treino_dados, treino_marcacoes)
    
    resultado = modelo.predict(teste_dados)
    acertos = resultado == teste_marcacoes
    
    total_de_acertos = sum(acertos)
    total_de_elementos = len(teste_dados)
    taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos
    
    print("Taxa de acerto do algoritmo: %f" % taxa_de_acerto)

df = pd.read_csv('busca.csv')

X_df = df[['home','busca','logado']]
Y_df = df['comprou']

Xdummies_df = pd.get_dummies(X_df).astype(int)
Ydummies_df = Y_df

X = Xdummies_df.values
Y = Ydummies_df.values

porcentagem_treino = 0.8
porcentagem_teste = 0.1

tamanho_de_treino = int(porcentagem_treino * len(Y))
tamanho_de_teste = int(porcentagem_teste * len(Y))
tamanho_validacao = len(Y) - tamanho_de_treino - tamanho_de_teste

treino_dados = X[:tamanho_de_treino]
treino_marcacoes = Y[:tamanho_de_treino]

teste_dados = X[tamanho_de_treino:(tamanho_de_treino+tamanho_de_teste)]
teste_marcacoes = Y[tamanho_de_treino:(tamanho_de_treino+tamanho_de_teste)]

validacao_dados = X[-tamanho_validacao:]
validacao_marcacoes = Y[-tamanho_validacao:]


modeloMultinomial = MultinomialNB()
fit_and_predict(modeloMultinomial,treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)
modeloAdaBoost = AdaBoostClassifier()
fit_and_predict(modeloAdaBoost,treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)

print(f"Total de teste: {len(teste_dados)}")

acerto_base = max(Counter(teste_marcacoes).values())
taxa_de_acerto_base = acerto_base * 100 / len(teste_marcacoes)
print(f'taxa de acerto base: {taxa_de_acerto_base}%')
