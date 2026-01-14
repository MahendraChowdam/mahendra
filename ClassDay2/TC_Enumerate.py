fruits=['apple','orange','banana']
for index,value in enumerate(fruits):
    print(index,value)


from enum import Enum

class Color(Enum):
    Red=1
    Green=2
    Blue=3
print(Color.Red.value,Color.Red.name)
#print(Color.Red.name)