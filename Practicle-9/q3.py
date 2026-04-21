import mysql.connector

# Step 1: Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",   # change if needed
    database="demo_data"
)

mycursor = mydb.cursor()

# Step 2: Execute SELECT query
mycursor.execute("SELECT * FROM doctor_details")

# Step 3: Fetch all records
result = mycursor.fetchall()

# Step 4: Display data
print("Doctor Details:\n")

for row in result:
    print(row)