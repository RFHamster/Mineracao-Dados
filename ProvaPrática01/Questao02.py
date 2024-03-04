import pandas as pd

# a) Carregar o arquivo num dataset do pandas
dataset = pd.read_csv("/content/sample_data/pedreiros.csv")
print("A")
print(dataset)

print("------------------------------------------------------")

# b) Retirar registros nulos e armazená-los em outra tabela
dataset_sem_nulos = dataset.dropna()
registros_nulos = dataset[dataset.isnull().any(axis=1)]
print("B")
print("Registros Nulos")
print(registros_nulos)
print("Tabela sem Nulos")
print(dataset_sem_nulos)

print("------------------------------------------------------")

# c) Mostrar como os dados estão organizados
print("Quantidade de linhas e colunas:", dataset.shape)
print("O que tem nas colunas:", dataset.columns.tolist())

print("------------------------------------------------------")

# d) Gerar o sumário dos dados
sumario = dataset.describe(include='all')
print("D")
print(sumario)

print("------------------------------------------------------")

# e) Gerar relatórios com salários específicos
print("E")
## Escolhendos os salários entre as datas de 1820 e 1840
relatorio_1 = dataset[(dataset['data'] >= 1820) & (dataset['data'] <= 1840)]
print("Salários entre as datas 1820 e 1840")
print(relatorio_1)
## Escolhendos os salários maiores ou iguais 180000,00
relatorio_2 = dataset[dataset['salario'] >= 180000.00]
print("Salário a partir de 180.000,00")
print(relatorio_2)