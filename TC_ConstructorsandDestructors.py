class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        print("constructor called")
    def __del__(self):
        print("destructor called")

e = employee("mahi",50000)
print(e.name,e.salary)
print(e.salary)