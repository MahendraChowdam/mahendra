from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["companydb"]

collection = db["Employee"]

result = collection.insert_one({"name": "Reddy", "age": 32, "salary": "45000"})

result1 = collection.find({"name": "Reddy"})

documents = list(result1)

print(documents)