from functools import reduce

numbers = range(1, 21)
even_numbers = filter(lambda x: x % 2 == 0, numbers)
squared_numbers = map(lambda x: x * x, even_numbers)
result = reduce(lambda a, b: a + b, squared_numbers)

print(result)
