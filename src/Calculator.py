def addition_of_two_numbers(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return num1 + num2

def subtraction_of_two_numbers(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return num2 - num1

def multiplication_of_two_numbers(num1, num2):
    c = num1 * num2
    return c

def division_of_two_numbers(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return round(num2 / num1, 7)

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, num1, num2):
        self.result = addition_of_two_numbers(num1, num2)
        return self.result

    def subtract(self, num1, num2):
        self.result = subtraction_of_two_numbers(num1, num2)
        return self.result

    def multiply(self, num1, num2):
        self.result = multiplication_of_two_numbers(num1, num2)
        return self.result

    def divide(self, num1, num2):
        self.result = round(division_of_two_numbers(num1, num2), 7)
        return self.result
