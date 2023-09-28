import csv
from utilities.settings import BASE_DIR

# Directory path
path = BASE_DIR / 'TestData/DataForTest.csv'
path2 = BASE_DIR / 'TestData/DataForTestCreateAccount.csv'


class utils:
    @staticmethod
    def read_data_from_csv(filename=path):
        data_list = []
        with open(filename, mode='r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                data_list.append(row)
        return data_list

    @staticmethod
    def read_data_from_csv_create_user(filename=path2):
        data_list2 = []
        with open(filename, mode='r', newline='') as csv_file2:
            csv_reader2 = csv.reader(csv_file2)
            for row in csv_reader2:
                data_list2.append(row)
        return data_list2