# Seguda Atividade Avaliativa Mineração de Dados

## Objetivo do database:

Usar atributos biomecânicos para classificar os pacientes de acordo com os rótulos presentes em cada dataset.

## Contextualização dos dados:

Cada paciente é representado no conjunto de dados por seis atributos biomecânicos derivados daforma e orientação da pelve e da coluna lombar (cada um é uma coluna):

  * incidência pélvica
  * inclinação pélvica
  * ângulo de lordose lombar
  * inclinação sacral
  * rádio pélvico
  * grau de espondilolistese
  
Os dados foram organizados em dois arquivos de classificação diferentes, mas correlacionados.

  * column_2C_weka.csv (arquivo com dois rótulos de classe): as categorias Hérnia de Disco e Espondilolistese foram fundidas em uma única categoria rotulada como 'anormal'. Assim, neste arquivo contém dados para  classificar os pacientes comopertencentes a uma de duas categorias: Normal (100 pacientes) ou Anormal (210 pacientes).
  * column_3C_weka.csv (arquivo com três rótulos de classe): esse arquivo consiste em classificar os pacientes como pertencentes a uma das três categorias: Normal (100 pacientes), Hérnia de Disco (60 pacientes) ou Espondilolistese (150 pacientes).

Todos os passos abaixo deverão ser realizados pelas duas bases de dados: column_2C_weka.csv ecolumn_3C_weka.csv

  2. Pré-processamento de dados: verifique se todas as instâncias possuem valores, e se for o caso remove instâncias com valores ausentes.
  3. Separe as instâncias aleatoriamente entre dados de treino e dados de teste.
  4. Usando o conjunto de dados de treino, realize aprendizagem para três tipos de classificação: o método de árvore de decisão, o método bayesiano, e o método de vetores SVM.
  5. Usando os três métodos, realize classificação pelo conjunto de teste.
  6. Verifique a acurácia de classificação para os três métodos usando as classes fornecidas junto comos dados medida como o número de instâncias com classes corretas dividido por o número de instâncias de teste.
  
O aluno deve submeter o código que realiza todos os passos acima. O código deve imprimir todosos passos realizados terminando com a descrição da acurácia/precisão de cada classificação realizada pelo conjunto de teste.