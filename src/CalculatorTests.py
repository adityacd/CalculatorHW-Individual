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
            # the second column in the text line is y value.
            y = row['Value 2']
            # the third column in the text line is (x + y) value.
            expect_result = int(row['Result'])
            self.assertEqual(self.calobject.add(x, y), expect_result)
            self.assertEqual(self.calobject.result, expect_result)

    def test_subtraction_method_calculator(self):
        test_data = CsvReader('./src/Unit Test Subtraction.csv').data
        for row in test_data:
            x = row['Value 1']
            # the second column in the text line is y value.
            y = row['Value 2']
            # the third column in the text line is (x + y) value.
            expect_result = int(row['Result'])
            self.assertEqual(self.calobject.subtract(x, y), expect_result)
            self.assertEqual(self.calobject.result, expect_result)
            #self.assertEqual(self.calobject.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            #self.assertEqual(self.calobject.result, int(row['Result']))

    def test_multiply_method_calculator(self):
        test_data = CsvReader('./src/Unit Test Multiplication.csv').data
        for row in test_data:
            x = int(row['Value 1'])
            # the second column in the text line is y value.
            y = int(row['Value 2'])
            # the third column in the text line is (x + y) value.
            expect_result = int(row['Result'])
            self.assertEqual(self.calobject.multiply(x, y), expect_result)
            self.assertEqual(self.calobject.result, expect_result)
            #self.assertEqual(self.calobject.multiply(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            #self.assertEqual(self.calobject.result, int(row['Result']))

    def test_divide_method_calculator(self):
        test_data = CsvReader('./src/Unit Test Division.csv').data
        for row in test_data:
            x = float(row['Value 1'])
            y = float(row['Value 2'])
            z = float(row['Result'])
            self.assertEqual(self.calobject.divide(x, y), round(z, 7))
            self.assertEqual(self.calobject.result, round(z, 7))

if __name__ == '__main__':  # This is just causing the unitttest to run
    unittest.main()
