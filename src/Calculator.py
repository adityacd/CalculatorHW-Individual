def addition_of_two_numbers(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return num1 + num2


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, num1, num2):
        self.result = addition_of_two_numbers(num1, num2)
        return self.result
