from scipy.stats import skew, kurtosis

class AnalizeyDatas:

    @staticmethod
    def skew_datas(datas):
        return skew(datas)

    @staticmethod
    def kurt_datas(datas):
        return kurtosis(datas)



