import pandas as pd
from sklearn.preprocessing import Normalizer
from sklearn.cluster import KMeans, AgglomerativeClustering
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Leitura e Pré-Processamento de Nulos
seeds_data = pd.read_csv('/content/phpPrh7lv.csv', na_values=['NA']).drop(['Class'], axis=1)


# Remoção de Atributos Dependentes - Remoção dos 3 Mais Dependentes
corr_matrix = seeds_data.corr()
avg = {}

for column in corr_matrix:
    current_avg = 0

    for row in corr_matrix:
        current_avg += corr_matrix[column][row]
    avg[column] = current_avg / 8

independent_attributes = sorted(avg.items(), key=lambda x:x[1], reverse=True)[:3]

for atb in independent_attributes:
    seeds_data = seeds_data.drop(atb[0], axis=1)

# Normalização
normalized_seeds_data = Normalizer().fit(seeds_data).transform(seeds_data)

# K-Média com 3 Grupos
clusters3_km = KMeans(n_clusters=3,init='random')
clusters3_km.fit(normalized_seeds_data)
clusters3_prediction = clusters3_km.predict(normalized_seeds_data)

# K-Média com 4 Grupos
clusters4_km = KMeans(n_clusters=4,init='random')
clusters4_km.fit(normalized_seeds_data)
clusters4_prediction = clusters4_km.predict(normalized_seeds_data)

print(clusters3_prediction)
print(clusters4_prediction)

# Coesão e separação dos agrupamentos
sse_3 = clusters3_km.inertia_
sse_4 = clusters4_km.inertia_

print("SSE com 3 Grupos:", sse_3)
print("SSE com 4 Grupos:", sse_4)

# Agrupamento Hierárquico
agglomerative_model = AgglomerativeClustering(n_clusters=3)
agglomerative_prediction = agglomerative_model.fit_predict(normalized_seeds_data)

# Dendrograma
linked = linkage(normalized_seeds_data, 'ward')
plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)
plt.title('Dendrograma Hierárquico')
plt.xlabel('Índices dos registros')
plt.ylabel('Distância')
plt.show()