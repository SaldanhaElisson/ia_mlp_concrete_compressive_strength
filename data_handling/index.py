from data_main import DataMain
from cleassing_datas import CleasingDatas

path_file = "../concrete_data.xls"
data_main = DataMain(path_file=path_file)
## Gerar os gráficos sem tirar os outilers
# data_main.create_all_histogram()

## Utilizei o critério de caixa para tirar os outliers
data_cleaned, num_outliers = CleasingDatas.remove_outliers(data_main.data_set)

data_main_cleaned = DataMain(data_frame=data_cleaned)

data_frame = data_main_cleaned.data_set

# Exportar para um arquivo CSV

## Gerar os gráficos tirando os outlers
# data_main_cleaned.create_all_histogram()

print(f"Número de outliers removidos: {num_outliers}")
print(f"Dados sem outliers:\n{data_cleaned}")

