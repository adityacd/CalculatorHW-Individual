def addition_of_two_numbers(a, b):
    a = int(a)
    b = int(b)
    return a + b

def subtraction_of_two_number(a, b):
    a = int(a)
    b = int(b)
    return b - a

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
