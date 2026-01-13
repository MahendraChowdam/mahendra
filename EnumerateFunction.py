from functools import reduce

numbers = range(1, 21)
even_numbers = filter(lambda x: x % 2 == 0, numbers)
squared_numbers = list(map(lambda x: x * x, even_numbers))

for index, value in enumerate(squared_numbers):
    print(index, value)
