from models.person import Person
from utils.descriptors import MarksDescriptor
from utils.decorators import log_execution, time_it

class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, sid, name, department, semester, marks):
        super().__init__(sid, name, department)
        self.semester = semester
        self.marks = marks

    def get_details(self):
        print("Student Details")
        print("--------------------------------")
        print(f"Name      : {self.name}")
        print("Role      : Student")
        print(f"Department: {self.department}")

    @log_execution
    @time_it
    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
        print(f"Average: {avg:.1f}")
        print(f"Grade  : {grade}")
        return avg

    def __gt__(self, other):
        return self.calculate_performance() > other.calculate_performance()
