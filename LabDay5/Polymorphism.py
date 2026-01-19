# Step 1: Define the base class
class Calculator:
    def calculate(self, a, b):
        return a + b


# Step 2: Define the derived class (method overriding)
class AdvancedCalculator(Calculator):
    def calculate(self, a, b):
        return a * b


# Step 3: Operator overloading example
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)


# Step 4: Object creation and polymorphism demonstration
calc = Calculator()
adv_calc = AdvancedCalculator()

print("Calculator result:", calc.calculate(5, 3))
print("AdvancedCalculator result:", adv_calc.calculate(5, 3))

n1 = Number(10)
n2 = Number(20)
n3 = n1 + n2

print("Result of adding two Number objects:", n3)

