from models.student import Student
from models.faculty import Faculty
from models.course import Course
from services.file_service import save_students_json, generate_csv_report
from utils.generators import student_generator

students = []
faculty_list = []
courses = []

while True:
    print("""
1 Add Student
2 Add Faculty
3 Add Course
4 Calculate Performance
5 Generate Reports
6 Exit
""")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            s = Student(
                input("ID: "),
                input("Name: "),
                input("Department: "),
                int(input("Semester: ")),
                list(map(int, input("Marks: ").split()))
            )
            students.append(s)
            print("Student Created Successfully")

        elif choice == "2":
            f = Faculty(
                input("ID: "),
                input("Name: "),
                input("Department: "),
                int(input("Salary: "))
            )
            faculty_list.append(f)
            print("Faculty Created Successfully")

        elif choice == "3":
            faculty = faculty_list[0]
            c = Course(
                input("Code: "),
                input("Course Name: "),
                int(input("Credits: ")),
                faculty
            )
            courses.append(c)
            print("Course Added Successfully")

        elif choice == "4":
            students[0].calculate_performance()

        elif choice == "5":
            save_students_json(students)
            generate_csv_report(students)

        elif choice == "6":
            print("Thank you for using Smart University Management System")
            break

    except Exception as e:
        print("Error:", e)