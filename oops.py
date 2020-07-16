class Calculator:
    num = 10

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b

    def greet(self, name):
        print('Good morning, ' + name)

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(10, 20)
obj.greet('Priyesh')

print(obj.summation())
