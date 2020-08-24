import pandas as pd


class DDT:

    @staticmethod
    def read_csv_toList(column_list):
        data_path = 'C:\\PycharmProjects\\AutoTest\\pyselenium\\csv_data\\search_data.csv'
        csv_data = pd.read_csv(data_path, encoding='utf-8')
        data_list = csv_data[column_list].values.tolist()
        print(data_list)
        return data_list

    @staticmethod
    def read_csv_toDict():
        data_path = 'C:\\PycharmProjects\\AutoTest\\pyselenium\\csv_data\\testCaseName_data.csv'
        csv_data = pd.read_csv(data_path, encoding='utf-8')
        data_list = csv_data[['jenkins_case_name', 'pytest_case_name']].values.tolist()
        data_dict = dict(data_list)
        print(data_dict)
        return data_dict


if __name__ == '__main__':
    DDT.read_csv_toDict()