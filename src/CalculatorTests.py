import unittest

from Calculator import Calculator

from CsvReading import CsvReader

class MyTestCase(unittest.TestCase):  # Accessing the methods

    def setUp(self) -> None:
        self.calobject = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calobject, Calculator)

    def test_add_method_calculator(self):
        test_data = CsvReader('./src/csvfiles/Unit Test Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calobject.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calobject.result, int(row['Result']))



if __name__ == '__main__':  # This is just causing the unitttest to run
    unittest.main()
