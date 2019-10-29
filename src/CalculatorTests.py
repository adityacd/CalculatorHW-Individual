import unittest

from Calculator import Calculator


class MyTestCase(unittest.TestCase):  # Accessing the methods

    def setUp(self) -> None:
        self.calobject = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calobject, Calculator)



if __name__ == '__main__':  # This is just causing the unitttest to run
    unittest.main()
