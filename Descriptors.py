
class Salary:
    def __get__(self, obj, objtype=None):
        return obj._salary

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("Salary must be a positive number")
        obj._salary = value

class Employee:
    salary = Salary()   # Descriptor

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary   # Goes through descriptor



e1 = Employee("Mahendra", 30000)
e2 = Employee("Ravi", 45000)

print(e1.name, e1.salary)
print(e2.name, e2.salary)

# This will raise an error
#e3 = Employee("Anil", -20000)
