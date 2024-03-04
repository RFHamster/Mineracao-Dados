## Aminoacidos tem todas as letras do alfabeto menos J,O,U
## https://labs.icb.ufmg.br/lbcd/grupo4/simbol.html
aminoacidos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

## Calculando a Distância Minkowski (Manhatan -> p = 1 e Euclidiana -> p = 2)
def distancia_minkowski(ponto1, ponto2, p):
  soma = 0
  ## Calculando o soma dos módulos da diferença de cada atributo
  for i in aminoacidos:
    soma += (abs(ponto1[i] - ponto2[i])) ** p
  ## Tirando a raiz p da soma para descobrir o total
  return soma ** (1/p)

## Calculando a Distância Supremmum
def distancia_supremum(ponto1, ponto2):
  # Considerando uma minowiski onde p tende ao infinito
  return max(abs(ponto1[i] - ponto2[i]) for i in aminoacidos)

## Calculando o produto interno de dois vetores
def produto_interno(ponto1, ponto2):
  soma = 0
  ## Calculando a soma dos produtos de cada atributo (produto interno)
  for i in aminoacidos:
    soma += ponto1[i] * ponto2[i]
  return soma

def comprimento_vetor(ponto1):
  soma = 0
  ## Calculando a soma dos atributo elevado ao quadrado
  for i in aminoacidos:
    soma += ponto1[i] ** 2
  ## Tirar a raiz da soma para produzir o comprimento
  return soma ** 0.5

## Calculando a similaridade cossenos
##(produto interno de x e y, dividido pelo produto dos comprimentos)
def similaridade_cosseno(ponto1, ponto2):
  return (produto_interno(ponto1, ponto2)/(comprimento_vetor(ponto1)*comprimento_vetor(ponto2)))

vetor = {}

# Populando o vetor que irá armazenar a quantidade de aparecimento de cada aminoacido
for animal, sequenciamento in sequenciamentos.items():
  vetor[animal] = {}
  ## Iniciando todas as contagens como 0
  for letra in aminoacidos:
    vetor[animal][letra] = 0
  ## Toda vez que o aminoacido aparecer, sua contagem é incrementada
  for aminoacido in sequenciamento:
    vetor[animal][aminoacido] += 1

print("Vetor Ocorrencia Aminoacidos")
print(vetor)
# Comparando todos os objetos entre si
print("----------------------------------------------------")
print("Distancias Cavalo x Hamster")
print("Distancia Manhatham")
print(distancia_minkowski(vetor['cavalo'], vetor['hamster'], 1))
print("Distancia Euclidiana")
print(distancia_minkowski(vetor['cavalo'], vetor['hamster'], 2))
print("Distancia Supremum")
print(distancia_supremum(vetor['cavalo'], vetor['hamster']))
print("Similaridade de Cossenos")
print(similaridade_cosseno(vetor['cavalo'], vetor['hamster']))
print("----------------------------------------------------")
print("Distancias Cavalo x Rato")
print("Distancia Manhatham")
print(distancia_minkowski(vetor['cavalo'], vetor['rato'], 1))
print("Distancia Euclidiana")
print(distancia_minkowski(vetor['cavalo'], vetor['rato'], 2))
print("Distancia Supremum")
print(distancia_supremum(vetor['cavalo'], vetor['rato']))
print("Similaridade de Cossenos")
print(similaridade_cosseno(vetor['cavalo'], vetor['rato']))
print("----------------------------------------------------")
print("Distancias Hamster x Rato")
print("Distancia Manhatham")
print(distancia_minkowski(vetor['hamster'], vetor['rato'], 1))
print("Distancia Euclidiana")
print(distancia_minkowski(vetor['hamster'], vetor['rato'], 2))
print("Distancia Supremum")
print(distancia_supremum(vetor['hamster'], vetor['rato']))
print("Similaridade de Cossenos")
print(similaridade_cosseno(vetor['hamster'], vetor['rato']))