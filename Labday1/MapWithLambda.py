numbers = range(1, 21)


even_numbers = filter(lambda x: x % 2 == 0, numbers)


squared_numbers = list(map(lambda x: x * x, even_numbers))

print(squared_numbers)
