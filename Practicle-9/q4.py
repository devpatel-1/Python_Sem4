import mysql.connector

# Step 1: Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",   # change if needed
    database="demo_data"
)

mycursor = mydb.cursor()

# Step 2: Execute JOIN query
query = """
SELECT d.*
FROM doctor_details d
JOIN hospital_details h
ON d.Hospital_Id = h.Hospital_Id
WHERE h.Hospital_Name = 'Janta'
"""

mycursor.execute(query)

# Step 3: Fetch data
result = mycursor.fetchall()

# Step 4: Display
print("Doctors in Janta Hospital:\n")

for row in result:
    print(row)