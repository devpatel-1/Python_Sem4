import mysql.connector

# Step 1: Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",   # change if needed
    database="demo_data"
)

mycursor = mydb.cursor()

# Step 2: Drop table
mycursor.execute("DROP TABLE hospital_details")

print("Table 'hospital_details' deleted successfully!")