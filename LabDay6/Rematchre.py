import re


def check_employee_id(emp_id):
    pattern = r'^EMP\d{3}'

    if re.match(pattern, emp_id):
        print("Valid Employee ID")
    else:
        print("Invalid Employee ID")


# Example usage
emp_id = input("Enter Employee ID: ")
check_employee_id(emp_id)
