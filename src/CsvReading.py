import csv
from pprint import pprint


class CsvReader:  # Created the Class CsvReader.
    data = []

    def __init__(self, filepath):  # Constructor of the class.
        self.data = []
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')  # Reading the .csv files
            for row in csv_data:
                self.data.append(row)
        pprint(self.data)
        pass
