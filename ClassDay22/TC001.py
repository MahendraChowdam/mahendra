import mysql.connector
host = "localhost"
user = "root"
password = "root"
database = "feb2026"


conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = conn.cursor()
print("connect success")
query="select * from feb2026.emp_table"
cursor.execute(query)

result = cursor.fetchall()

for row in result:
    print(row)


