import pandas as pd
from data_handling.charts import Charts


class DataMain:
    def __init__(self, path_file=None, data_frame=None):
        if path_file:
            self.data_set = pd.read_excel(path_file)
        elif data_frame is not None:
            self.data_set = data_frame
        self.cement = self.data_set.iloc[:, 0]
        self.blast_fumace_slag = self.data_set.iloc[:, 1]
        self.fly_ash = self.data_set.iloc[:, 2]
        self.water = self.data_set.iloc[:, 3]
        self.superplasticizer = self.data_set.iloc[:, 4]
        self.course_aggregate = self.data_set.iloc[:, 5]
        self.fine_aggregate = self.data_set.iloc[:, 6]
        self.age = self.data_set.iloc[:, 7]




    def create_histogram_cement(self):
        histogram_cement_chart = Charts()
        histogram_cement_chart.histogram(self.cement, "Cement (Kg|m³)")

    def create_histogram_blast_fumace_slag(self):
        histogram_blast_fumace_slag_chart = Charts()

        histogram_blast_fumace_slag_chart.histogram(self.blast_fumace_slag, "Blast Fumace Slag (Kg|m³)")

    def create_histogram_fly_ash(self):
        histogram_fly_ash_chart = Charts()
        histogram_fly_ash_chart.histogram(self.fly_ash, "Fly Ash (Kg|m³)")

    def create_histogram_water(self):
        histogram_water_chart = Charts()
        histogram_water_chart.histogram(self.water, "Water (Kg|m³)")

    def create_histogram_superplasticizer(self):
        histogram_superplasticizer_chart = Charts()
        histogram_superplasticizer_chart.histogram(self.superplasticizer, "Superplasticizer (Kg|m³)")

    def create_histogram_course_aggregate(self):
        histogram_course_aggregate_chart = Charts()
        histogram_course_aggregate_chart.histogram(self.course_aggregate, "Courage aggregate (Kg|m³)")

    def create_histogram_fine_aggregate(self):
        histogram_fine_aggregate_chart = Charts()
        histogram_fine_aggregate_chart.histogram(self.fine_aggregate, "Fine Aggregate (Kg|m³)")

    def create_histogram_age(self):
        histogram_age_chart = Charts()
        histogram_age_chart.histogram(self.age, "Age (day)" )

    def create_all_histogram(self):
        self.create_histogram_cement()
        self.create_histogram_blast_fumace_slag()
        self.create_histogram_fly_ash()
        self.create_histogram_water()
        self.create_histogram_superplasticizer()
        self.create_histogram_course_aggregate()
        self. create_histogram_fine_aggregate()
        self.create_histogram_age()
