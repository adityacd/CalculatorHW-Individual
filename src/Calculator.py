def addition_of_two_numbers(a, b):
    a = int(a)
    b = int(b)
    return a + b

def subtraction_of_two_number(a, b):
    a = int(a)
    b = int(b)
    return b - a

def multiplication_of_two_number(num1, num2):
    c = num1 * num2
    return c

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition_of_two_numbers(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction_of_two_number(a, b)
        return self.result

    def multiply(self, num1, num2):
        self.result = multiplication_of_two_number(num1, num2)
        return self.result
