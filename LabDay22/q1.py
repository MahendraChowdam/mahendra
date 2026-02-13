import mysql.connector

# Database connection details
host = "localhost"
user = "root"
password = "root"
database = "company_db"

# Connect to MySQL database
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conn.cursor()
print("Connected to database successfully")

# -------------------------------------------------
# 1. Fetch employees with salary > 50,000
# -------------------------------------------------
print("\nEmployees with salary greater than 50,000:")
select_query = """
SELECT emp_id, emp_name, emp_dep, salary
FROM employee
WHERE salary > 50000
"""
cursor.execute(select_query)

for row in cursor.fetchall():
    print(row)

# -------------------------------------------------
# 2. Insert a new employee record
# -------------------------------------------------
insert_query = """
INSERT INTO employee (emp_id, emp_name, emp_dep, salary)
VALUES (%s, %s, %s, %s)
"""
new_employee = (401, "Suresh", "IT", 65000)

cursor.execute(insert_query, new_employee)
conn.commit()
print("\nNew employee inserted successfully")

# -------------------------------------------------
# 3. Update salary of a specific employee by 10%
# -------------------------------------------------
employee_id = 401

update_query = """
UPDATE employee
SET salary = salary * 1.10
WHERE emp_id = %s
"""
cursor.execute(update_query, (employee_id,))
conn.commit()

print(f"\nSalary updated by 10% for employee ID {employee_id}")

# -------------------------------------------------
# Close database connection
# -------------------------------------------------
cursor.close()
conn.close()
print("\nDatabase connection closed")

