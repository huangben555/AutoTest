import pandas as pd


class DDT:

    @staticmethod
    def read_CSV(column_list):
        data_path = 'C:\\PycharmProjects\\AutoTest\\pyselenium\\csv_data\\search_data.csv'
        csv_data = pd.read_csv(data_path, encoding='utf-8')
        data_list = csv_data[column_list].values.tolist()
        print(data_list)
        return data_list
