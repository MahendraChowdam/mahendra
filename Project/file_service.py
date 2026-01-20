import json
import csv

def save_students_json(students):
    data = []
    for s in students:
        data.append({
            "id": s.id,
            "name": s.name,
            "department": s.department,
            "semester": s.semester,
            "marks": s.marks
        })

    with open("data/students.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Student data successfully saved to students.json")


def generate_csv_report(students):
    with open("data/students_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Department", "Average", "Grade"])

        for s in students:
            avg = sum(s.marks) / len(s.marks)
            grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
            writer.writerow([s.id, s.name, s.department, f"{avg:.1f}", grade])

    print("CSV Report Generated")
