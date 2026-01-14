from ctypes import pythonapi


class Student:
    name = "Ravi"
    age = 25

s1 = Student()
print(s1.name)
print(s1.age)


class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age

emp = Employee("mahi",23)
print(emp.name , emp.age)
print(emp.name)
print(emp.age)


class Driver:
    name = "suresh"
    age = 25
    salary = 25000
    dept = "driver"


dri = Driver()

print(dri.name, dri.age, dri.salary)

class Teacher:
    def __init__(self,name,age,salary,sub):
        self.name = name
        self.age = age
        self.salary = salary
        self.sub = sub
tech = Teacher("mahi",30,50000,"python")
print(tech.name, tech.age, tech.salary)
