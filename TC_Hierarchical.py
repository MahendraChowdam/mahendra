class Parent:
    def parent(self):
        print("Parent")

class Child1(Parent):
    def child1(self):
        print("Child1")
class Child2(Parent):
    def child2(self):
        print("Child2")

c1 = Child1()
c1.child1()
c1.parent()

c2 = Child2()
c2.child2()
c2.parent()