import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Harish@2006",
    database="demo"
)

cursor = conn.cursor()

query = "SELECT * FROM ml" 

cursor.execute(query)

results = cursor.fetchall()

for row in results:
    print(row)
cursor.close()
conn.close()
