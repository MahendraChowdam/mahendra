class Department:
    def __init__(self, dept_id, name):
        self.dept_id = dept_id
        self.name = name
        self.students = []
        self.faculty = []

    def add_student(self, student):
        self.students.append(student)

    def add_faculty(self, faculty):
        self.faculty.append(faculty)

    def get_details(self):
        print("Department Details")
        print("--------------------------------")
        print(f"Department ID : {self.dept_id}")
        print(f"Department    : {self.name}")
        print(f"Total Students: {len(self.students)}")
        print(f"Total Faculty : {len(self.faculty)}")
