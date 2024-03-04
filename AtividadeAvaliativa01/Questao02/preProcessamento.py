df=pandas.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv ',sep=';')
array=df.values
# Separando os dados em entradas e saídas
x=array[:,0:8]
y=array[:,8]
print("Dados Brutos")
print("x (entradas)")
print(x)
print("----------------------------------------------------")
#(saída -> pH (nesse caso, caso queira qualidade é o 11 no lugar do 8))
print("y (saida)")
print(y)

print("----------------------------------------------------")

## Normalizando os dados
print("Normalizações")

# Utilizando MinMaxScaler, vai colocar eles na escala de 0 a 1 (uma normalização mais fraca, porque generiza para qualquer escala) (meio que uma gambiarra para normalizar)
print("Normalização com MinMaxScaler")
scaler=MinMaxScaler(feature_range=(0,1))
rescaledX=scaler.fit_transform(x)
numpy.set_printoptions(precision=3)
rescaledX[0:5,:]
print(rescaledX)
print("----------------------------------------------------")
# Utilizando a classe Normalizer (mais aconselhavel)
print("Normalização com classe Normalizer")
scaler=Normalizer().fit(x)
normalizedX=scaler.transform(x)
normalizedX[0:5,:]
print(normalizedX)

print("----------------------------------------------------")

## Transformação Gaussiana
print("Transformação Gaussiana com classe Standard Scaler")
scaler=StandardScaler().fit(x)
rescaledX=scaler.transform(x)
rescaledX[0:5,:]
print(rescaledX)

print("----------------------------------------------------")

## Binarização dos Dados
print("Binarização dos Dados")
binarizer=Binarizer(threshold=0.0).fit(x)
binaryX=binarizer.transform(x)
binaryX[0:5,:]
print(binaryX)

print("----------------------------------------------------")

## Remoção de Média (Centralizar atributos para o 0)
# Ver o quão perto ou longe os valores estão da parte central geral
print("Remoção de Média")
data_standardized=scale(df)
print("Média das características padronizadas ao longo do eixo 0")
print(data_standardized.mean(axis=0))
print("Desvio Padrão das características padronizadas ao longo do eixo 0")
print(data_standardized.std(axis=0))

print("----------------------------------------------------")

## One Hot Encoding
# Meio que uma mini-IA que vai tranformar, por exemplo, tipos de animais/cores, nesse caso tipo de vinho, em uma forma de categoria numérica
print("One Hot Encoding")
encoder=OneHotEncoder()
encoder.fit([[0,1,6,2],
[1,5,3,5],
[2,4,2,7],
[1,0,4,2]
])
print(encoder.transform([[2,4,3,5]]).toarray())

print("----------------------------------------------------")

## Codificação de Rótulos
# basicamente tem uns rótulos, transforma eles em números pra IA/código entender, e depois consegue reconverter para nós humanos entender
# Um ENUM mais bonitinho
print("Codificação de Rótulos")

label_encoder=LabelEncoder()
input_classes=['Havells','Philips','Syska','Eveready','Lloyd']
label_encoder.fit(input_classes)
for i,item in enumerate(label_encoder.classes_):
  print(item,'-->',i)

print("Retransformando")

labels=['Lloyd','Syska','Philips']
label_encoder.transform(labels)
label_encoder.inverse_transform(label_encoder.transform(labels))

print("----------------------------------------------------")

