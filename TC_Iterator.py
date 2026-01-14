data = [1,2,3]
it = iter(data)
print(next(it))
print(next(it))
print(next(it))

for i in [10,20,30,40,50]:
    print(i)

class Count:
    def __init__(self,limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration
obj = Count(10)

for i in obj:
    print(i)
