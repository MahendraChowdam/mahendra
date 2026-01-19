class Animal:
    def sound(self):
        print("Animal is sounding")
class Dog(Animal):
    def sound(self):
        print("Dog is barks")
class Cat(Animal):
    def sound(self):
        print("Cat is meows")
obj1 = [Dog(), Cat()]

for obj in obj1:
    obj.sound()