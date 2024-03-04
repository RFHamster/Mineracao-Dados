import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Produto':["Chocolate","Banana"],
    'Quantidade':[200,80],
    'Preco':[3.00,0.5]})
ser = pd.Series([600,40])

df.to_csv("vendas.csv")

admissoes = pd.read_csv('ipea_admissoes.csv')

ex2=admissoes[admissoes.iloc[:,0] >= 2018]
a2019=ex2[ex2['Data'].astype(str).str.contains('2019')]
print(a2019)

demissoes = pd.read_csv('ipea_demissoes.csv')
#print(demissoes.head())

# print("Tabela Demissoes: ")
# print("Linha e Colunas:")
# print(demissoes.shape)
# print("Indices:")
# print(demissoes.index)
# print("Colunas:")
# print(demissoes.columns)
# print("Descricao:")
# print(demissoes.info())
# print("Valores not null:")
# print(demissoes.count())

#print(admissoes.sum())
#print(admissoes.cumsum())

# a = pd.DataFrame({'a': [10,15,20,30,60]})
# a.sum()
# a.median()
# a.mean()

# a.boxplot()
# plt.show()