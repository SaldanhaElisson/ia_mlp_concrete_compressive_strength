from scipy.stats import kurtosis

from analizy_datas import AnalizeyDatas
import matplotlib.pyplot as plt
import numpy as np

class Charts:


    @staticmethod
    def law_sturges(data):
        len_data = len(data)
        ## Formula pra calcular Sturges
        qnt_class = int(1 + 3.322 * np.log10(len_data))
        return qnt_class


    def histogram(self, data, name_data):
        # Remover valores nulos
        data = data.dropna()
        assimetria = AnalizeyDatas.skew_datas(data)
        kurtosis = AnalizeyDatas.kurt_datas(data)
        print(f"Assimetria: {assimetria}")
        qnt_class = Charts.law_sturges(data)
        # Criar o histograma e a linha de densidade
        plt.hist(data, bins=qnt_class, edgecolor='black')
        plt.title(f'Histograma com Assimetria (Skewness = {assimetria:.2f}, Kurtosis = {kurtosis:.2f})')
        plt.xlabel(name_data)
        plt.ylabel('Frequência')
        plt.show()
