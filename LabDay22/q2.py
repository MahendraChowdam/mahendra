from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")

db = client["company_db"]
collection = db["Employees"]

# -------------------------------------------------
# 1. Insert a new employee document
# -------------------------------------------------
result = collection.insert_one({
    "name": "Ravi",
    "department": "IT",
    "salary": 60000
})

print("Inserted ID:", result.inserted_id)

# -------------------------------------------------
# 2. Find all employees in IT department
# -------------------------------------------------
result1 = collection.find({"department": "IT"})

documents = list(result1)
print("\nEmployees in IT department:")
print(documents)

# -------------------------------------------------
# 3. Update salary of an employee with given name
# -------------------------------------------------
collection.update_one(
    {"name": "Ravi"},
    {"$set": {"salary": 66000}}
)

print("\nSalary updated for Ravi")
