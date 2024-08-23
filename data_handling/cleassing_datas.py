class CleasingDatas:

    @staticmethod
    def remove_outliers(df):
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
        print(IQR)
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = ((df < lower_bound) | (df > upper_bound)).any(axis=1)
        return df[~outliers], outliers.sum()