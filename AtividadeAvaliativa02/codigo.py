## Importanto bibliotecas

import numpy as np
import pandas as pd
from sklearn.preprocessing import Normalizer
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn import svm

## Acuracia é quanto que ele acertou considerando todos os casos (1 em 10 por exemplo)
def makeAccuracy(Y_predct, Y_colinha):
  correto = 0
  for i in range(len(Y_predct)):
    if Y_predct[i] == Y_colinha[i]:
      correto += 1
  return (correto/len(Y_predct))

## Precisão é quanto que ele acertou considerando os positivos verdadeiros e os positivos falsos (vendo a precisão do acerto)
def makePrecision(Y_predct, Y_colinha, classe):
  TP = 0
  FP = 0
  for i in range(len(Y_predct)):
    if classe == Y_colinha[i]:
      if classe == Y_predct[i]:
        TP += 1
        continue
      FP += 1
  return (TP/(TP+FP))

# Função para fazer e treinar uma Arvore de Decisão
def makeTree(X_treino, Y_treino):
  clf = tree.DecisionTreeClassifier()
  clf = clf.fit(X_treino, Y_treino)
  #tree.plot_tree(clf)
  return clf

# Função para fazer e treinar o algoritmo com Bayes
def makeBayes(X_treino, Y_treino):
  clf = GaussianNB()
  clf = clf.fit(X_treino, Y_treino)
  return clf

# Função para fazer e treinar o algoritmo com Support Vector Machine
def makeSVM(X_treino, Y_treino):
  clf = svm.SVC()
  clf = clf.fit(X_treino, Y_treino)
  return clf

# Fazer testes com determinado algorimo e mostar a precisao e acuracia
def makePredict(clf, dataset, answer, classes):
  print("Predição")
  predct = clf.predict(dataset)
  print(predct)
  print("Colinha")
  print(answer)
  print("---------------------------------")
  print("Objeto Confusao")
  print(makeMatrizConfusao(predct,answer, classes))
  print("---------------------------------")
  print("Accuracy")
  print(makeAccuracy(predct, answer))
  print("Precision in classes: ")
  for classe in classes:
    print(classe)
    print(makePrecision(predct, answer,classe))
  print("-------------------------------------------------------------")

def separarDataset(dataset):
  x=dataset.values[:,0:6]
  y=dataset.values[:,6]

  ## Nomalizando meus valores de X
  scaler=Normalizer().fit(x)
  X_Normalized=scaler.transform(x)

  X_treino = x[:279]
  X_teste = x[-31:]
  Y_treino = y[:279]
  Y_teste = y[-31:]

  return X_treino, X_teste, Y_treino, Y_teste

## Fazer a Matriz Confusao
## Nesse caso ta mais para Objeto confusao, ele funciona mais ou menos assim
## As primeiras chaves do Objeto Confusao são as classes certas e cada uma dela possui outro objeto com as TODAS outras classes
## Isso representa a classe e quantas vezes ela foi classificada certamente e quantas vezes ela foi marcada como outra classe
## Com esses dados conseguimos deduzir os TP, FP, FN e TN dependendo do objeto que vamos analizar
def makeMatrizConfusao(predct, answer,classes):
  mConfusao = {}
  ## Iniciando todas as posicoes da matriz confusao como 0
  for classe in classes:
    mConfusao[classe] = {}
    for c in classes:
      mConfusao[classe][c] = 0

  for i in range(len(predct)):
    mConfusao[answer[i]][predct[i]] += 1

  return mConfusao

dados2C = pd.read_csv("/content/sample_data/column_2C_weka.csv")
dados3C = pd.read_csv("/content/sample_data/column_3C_weka.csv")

# print(dados2C)
# print(dados3C)

## Removendo valores nulos
dataset2c = dados2C.dropna()
dataset3c = dados3C.dropna()

# print(dataset2c)
# print(dataset3c)

## Aleatorizando meu dados, essa função pega a amostra aleatoriamente e remonta meu DataSet, embaralhado-o
## Vale ressalta que como ele pega aleatorio toda vez, cada vez que vc roda o problema a acuracia e precisao pode variar
dataset2c = dataset2c.sample(frac=1)
dataset3c = dataset3c.sample(frac=1)

## Separando meu dataSet (10% (31 tuplas) para teste e aprox 90% (279 tuplas) para treino)
X_treino2c, X_teste2c, Y_treino2c, Y_teste2c = separarDataset(dataset2c)
X_treino3c, X_teste3c, Y_treino3c, Y_teste3c = separarDataset(dataset3c)

# print(X_treino2c)
# print(Y_treino2c)
# print(X_teste2c)
# print(Y_teste2c)

# print(X_treino3c)
# print(Y_treino3c)
# print(X_teste3c)
# print(Y_teste3c)

classes2c = ["Abnormal", "Normal"]
## Fazendo, treinando e validando a arvore dos arquivos 2C
print("Arvore Binaria 2C")
clf = makeTree(X_treino2c,Y_treino2c)
makePredict(clf, X_teste2c, Y_teste2c,classes2c)

## Fazendo, treinando e validando a bayes dos arquivos 2C
print("Bayes 2C")
clf = makeBayes(X_treino2c,Y_treino2c)
makePredict(clf, X_teste2c, Y_teste2c,classes2c)

## Fazendo, treinando e validando a SVM dos arquivos 2C
print("SVM 2C")
clf = makeSVM(X_treino2c,Y_treino2c)
makePredict(clf, X_teste2c, Y_teste2c,classes2c)

classes3c = ["Spondylolisthesis", "Hernia", "Normal"]
## Fazendo, treinando e validando a arvore dos arquivos 3C
print("Arvore Binaria 3C")
clf = makeTree(X_treino3c,Y_treino3c)
makePredict(clf, X_teste3c, Y_teste3c,classes3c)

## Fazendo, treinando e validando a bayes dos arquivos 3C
print("Bayes 3C")
clf = makeBayes(X_treino3c,Y_treino3c)
makePredict(clf, X_teste3c, Y_teste3c,classes3c)

## Fazendo, treinando e validando a SVM dos arquivos 3C
print("SVM 3C")
clf = makeSVM(X_treino3c,Y_treino3c)
makePredict(clf, X_teste3c, Y_teste3c,classes3c)