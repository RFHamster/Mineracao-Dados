import pandas as pd
from sklearn.preprocessing import Normalizer
from sklearn import tree

dados = pd.read_csv("/content/sample_data/phpPrh7lv.csv")
#print(dados)

## Retirando registos nulos
dataset = dados.dropna()
x=dataset.values[:,0:7]
y=dataset.values[:,7]
# print(dataset)

scaler=Normalizer().fit(x)
X_Normalized=scaler.transform(x)
# print(datasetNormalized)

dataset_treino = X_Normalized[:200]
dataset_teste = X_Normalized[-10:]

Y_treino = y[:200]

#print(dataset_treino)
# print("---")
# print(dataset_teste)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(dataset_treino, Y_treino)

# tree.plot_tree(clf)

print(clf.predict(dataset_teste))




