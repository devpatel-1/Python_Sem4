import mysql.connector

# Step 1: Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",   # change if needed
    database="demo_data"
)

mycursor = mydb.cursor()

# Step 2: Update query
mycursor.execute("UPDATE doctor_details SET Experience = Experience + 1")

# Step 3: Save changes
mydb.commit()

print("Doctor experience updated successfully!")