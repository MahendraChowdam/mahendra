student={
    "name":"rahul",
    "age":20,
    "course":"python"
}

print(student)
print(student["name"])
print(student.get("age"))
print(student["course"])
student.pop("age")
print(student)
#student.popitem()
print(student)
print(student.keys())
print(student.values())
for key in student:
    print("key exists")

employees={
    101:{"name":"lela","sal":20000},
    102:{"name":"rahul","sal":20000},
}

print(employees[101]["name"])
