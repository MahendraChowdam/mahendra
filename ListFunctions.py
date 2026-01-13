numbers = [1, 2, 3, 4, 5]
names = ["ram", "hari", "suresh", "ramesh"]
mixed =[1, "python", 3.5]
print(numbers)
print(names)
print(mixed)

numbers[1] = 100
print(numbers)

for i in numbers:
    print(i)

if 10 in numbers:
    print("found")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])

names.reverse()
print(names)

names.extend(["pavan","lela"])
print(names)

names.append("ramo")
print(names)

names.remove("ramo")
print(names)

names.insert(2,"lali")