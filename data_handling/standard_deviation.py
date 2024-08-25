import pandas as pd

## Diretório onde o arquivo está localizado
df = pd.read_excel('C:/Users/icaro/Documents/development/faculdade/IA/concrete+compressive+strength/Concrete_Data.xls', engine='xlrd')

## Função para calcular a variância com precisão de 4 casas decimais
std = df.std().round(4)

print(std)