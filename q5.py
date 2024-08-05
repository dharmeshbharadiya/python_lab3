class Calculator:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def add(self):
        return self.__num1 + self.__num2

    def subtract(self):
        return self.__num1 - self.__num2

calc = Calculator(10, 5)

result = calc.add()
print("\nAddition:", result)

result = calc.subtract()
print("\nSubtraction:", result)
