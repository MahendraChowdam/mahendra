class Calculator:
    def calculate(self, a, b):
        return a + b


class AdvancedCalculator(Calculator):
    # Overriding the calculate method
    def calculate(self, a, b):
        return a * b
