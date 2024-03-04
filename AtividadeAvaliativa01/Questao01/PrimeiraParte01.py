from os import X_OK
# Transformar .asta em string
def read_fasta(arq):
  seq = ''
  with open(arq) as f:
    f.readline()
    for line in f:
      seq += line.strip()
  return seq

# Verificação Dissimilaridade Simples entre dois organismos
def d_simples(s1, s2):
  valoresIg = 0
  valoresTotal = len(s1)

  # Deixando as duas strings de tamanho igual, ignorando o que ultrapassar
  if len(s1) > len(s2):
    s1 = s1[:len(s2)]
  elif len(s2) > len(s1):
    valoresTotal = len(s2)
    s2 = s2[:len(s1)]

  # Vendo quantos valores iguais existem
  for i in range(valoresTotal):
    if s1[i] == s2[i]:
      valoresIg += 1

  # Retornando Total
  return (valoresTotal - valoresIg)/valoresTotal

# Caminhos arquivos
caminhoHamster = '/content/sample_data/hamster.fasta'
caminhoRato = "/content/sample_data/rat.fasta"
caminhoCavalo = "/content/sample_data/horse.fasta"

caminhos = {
    'hamster': caminhoHamster,
    'rato': caminhoRato,
    'cavalo': caminhoCavalo}

sequenciamentos = {}

# Colocando os sequenciamentos(string) em um chave valor
for animal, caminho in caminhos.items():
    sequenciamento = read_fasta(caminho)
    sequenciamentos[animal] = sequenciamento

print("Sequenciamento por Animal")
print(sequenciamentos)
print("----------------------------------------------------")
# Comparando todos os objetos entre si
cavalo_rato = d_simples(sequenciamentos['cavalo'], sequenciamentos['rato'])
print("Cavalo x Rato")
print(cavalo_rato)
print("----------------------------------------------------")
cavalo_hamster = d_simples(sequenciamentos['cavalo'], sequenciamentos['hamster'])
print("Cavalo x Hamster")
print(cavalo_hamster)
print("----------------------------------------------------")
hamster_rato = d_simples(sequenciamentos['hamster'], sequenciamentos['rato'])
print("Hamster x Rato")
print(hamster_rato)