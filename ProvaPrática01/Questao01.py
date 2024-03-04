import numpy as np
from scipy.spatial.distance import cosine, correlation, euclidean
from sklearn.metrics import jaccard_score

## Calculando o produto interno de dois vetores
def produto_interno(ponto1, ponto2):
  soma = 0
  ## Calculando a soma dos produtos de cada atributo (produto interno)
  for i in range(len(ponto1)):
    soma += ponto1[i] * ponto2[i]
  return soma

def comprimento_vetor(ponto1):
  soma = 0
  ## Calculando a soma dos atributo elevado ao quadrado
  for i in range(len(ponto1)):
    soma += ponto1[i] ** 2
  ## Tirar a raiz da soma para produzir o comprimento
  return soma ** 0.5

## Calculando a similaridade cossenos
##(produto interno de x e y, dividido pelo produto dos comprimentos)
def similaridade_cosseno(ponto1, ponto2):
  return (produto_interno(ponto1, ponto2)/(comprimento_vetor(ponto1)*comprimento_vetor(ponto2)))


print("A")
## Criando os Vetores
X_a = [1, 1, 1, 1]
Y_a = [2, 2, 2, 2]
print("Cosseno")
print(similaridade_cosseno(X_a, Y_a))
print("Correlação")
print(np.corrcoef(X_a, Y_a))
## Deu divisao por 0, std de X_a = 0
print("Euclidiana")
print(euclidean(X_a, Y_a))

print("------------------------------------------------------")

print("B")
## Criando os Vetores
X_b = np.array([0, 1, 0, 1])
Y_b = np.array([1, 0, 1, 0])
print("Cosseno")
print(similaridade_cosseno(X_b, Y_b))
print("Correlação")
print(np.corrcoef(X_b, Y_b)[0, 1])
print("Euclidiana")
print(euclidean(X_b, Y_b))
print("Jaccard")
print(jaccard_score(X_b, Y_b))

print("------------------------------------------------------")

print("C")
## Criando os Vetores
X_c = np.array([1, 1, 0, 1, 0, 1])
Y_c = np.array([1, 1, 1, 0, 0, 1])
print("Cosseno")
print(similaridade_cosseno(X_c, Y_c))
print("Correlação")
print(np.corrcoef(X_c, Y_c)[0, 1])
print("Jaccard")
print(jaccard_score(X_c, Y_c))
