class student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
    def display_details(self):
        print(self.name,"rollno:",self.rollno)

s1 = student("Ravi",1)
s2 = student("Mahi",2)
s1.display_details()
s2.display_details()
