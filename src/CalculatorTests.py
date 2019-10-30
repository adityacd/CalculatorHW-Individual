import unittest

from Calculator import Calculator

from CsvReading import CsvReader

class MyTestCase(unittest.TestCase):  # Accessing the methods

    def setUp(self) -> None:
        self.calobject = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calobject, Calculator)

    def test_addition_method_calculator(self):
        test_data = CsvReader('./src/Unit Test Addition.csv').data
        for row in test_data:
            x = row['Value 1']
            y = row['Value 2']
            expect_result = int(row['Result'])
            self.assertEqual(self.calobject.add(x, y), expect_result)
            self.assertEqual(self.calobject.result, expect_result)

    def test_subtraction_method_calculator(self):
        test_data = CsvReader('./src/Unit Test Subtraction.csv').data
        for row in test_data:
            x = row['Value 1']
            y = row['Value 2']
            expect_result = int(row['Result'])
            self.assertEqual(self.calobject.subtract(x, y), expect_result)
            self.assertEqual(self.calobject.result, expect_result)

    def test_multiply_method_calculator(self):
        test_data = CsvReader('./src/Unit Test Multiplication.csv').data
        for row in test_data:
            x = int(row['Value 1'])
            y = int(row['Value 2'])
            expect_result = int(row['Result'])
            self.assertEqual(self.calobject.multiply(x, y), expect_result)
            self.assertEqual(self.calobject.result, expect_result)

    def test_divide_method_calculator(self):
        test_data = CsvReader('./src/Unit Test Division.csv').data
        for row in test_data:
            x = float(row['Value 1'])
            y = float(row['Value 2'])
            expect_result = float(row['Result'])
            self.assertEqual(self.calobject.divide(x, y), round(expect_result, 7))
            self.assertEqual(self.calobject.result, round(expect_result, 7))

    def test_square_method_calculator(self):
        test_data = CsvReader('./src/Unit Test Square.csv').data
        for row in test_data:
            x = int(row['Value 1'])
            expect_result = int(row['Result'])
            self.assertEqual(self.calobject.square(x), expect_result)
            self.assertEqual(self.calobject.result, expect_result)

    def test_sqrt_method_calculator(self):
        test_data = CsvReader('./src/Unit Test Square Root.csv').data
        for row in test_data:
            x = float(row['Value 1'])
            expect_result = float(row['Result'])
            self.assertEqual(self.calobject.square_root(x), round(expect_result, 8))
            self.assertEqual(self.calobject.result, round(expect_result, 8))

if __name__ == '__main__':  # This is just causing the unitttest to run
    unittest.main()
