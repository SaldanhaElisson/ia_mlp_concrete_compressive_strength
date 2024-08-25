import pandas as pd
import seaborn as sns

# Diretório onde o arquivo está localizado
df = pd.read_excel('C:/Users/icaro/Documents/development/faculdade/IA/concrete+compressive+strength/Concrete_Data.xls', engine='xlrd')

# Criar a matriz de dispersão
pairplot = sns.pairplot(df)

# Salvar a matriz de dispersão
pairplot.savefig('matriz_dispersao.png')