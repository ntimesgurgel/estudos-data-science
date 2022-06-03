from dados import carregar_acessos
from sklearn.naive_bayes import MultinomialNB

X,Y = carregar_acessos()

treino_X = X[:int(len(X)*0.9)]
treino_Y = Y[:int(len(Y)*0.9)]

teste_X = X[int(len(X)*0.9):]
teste_Y = Y[int(len(Y)*0.9):]

modelo = MultinomialNB()
modelo.fit(treino_X,treino_Y)

resultado = modelo.predict(teste_X)
diferencas = resultado - teste_Y

acertos = [d for d in diferencas if d == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_Y)
taxa_de_acerto = 100 * total_de_acertos / total_de_elementos

print(taxa_de_acerto)
print(total_de_elementos)
