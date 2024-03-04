# Mostrar nossos dados
print("Mostrar nossos dados")
print(df.describe())

# Dimenções do DataSet
print("Dimenções do DataSet")
print(df.shape)

# Pegar um pedaço do DataSet
print("Primeira 10 tuplas do DataSet")
print(df.head(10))

# Agrupar Dados (Basicamente Contar, o que eu fiz ali dificil no codigo da questao 01 tinha pronto `o`)
print("Agrupando as atributos/valores de qualidade")
print(df.groupby('quality').size())