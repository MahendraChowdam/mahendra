class Count:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration


print("Iterator Output:")
for num in Count(5):
    print(num)

def count_gen(n):
    for i in range(1, n + 1):
        yield i


print("Generator Output:")
for num in count_gen(5):
    print(num)
