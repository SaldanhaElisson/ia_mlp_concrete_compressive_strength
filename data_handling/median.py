import pandas as pd

## Diretório onde o arquivo está localizado
df = pd.read_excel('C:/Users/icaro/Documents/development/faculdade/IA/concrete+compressive+strength/Concrete_Data.xls', engine='xlrd')

## Função para calcular a mediana com precisão de 4 casas decimais
median = df.median().round(4)

print(median)