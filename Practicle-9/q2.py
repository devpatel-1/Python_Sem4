import mysql.connector

# Step 1: Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",   # change if needed
    database="demo_data"
)

mycursor = mydb.cursor()

# Step 2: Create hospital_details table
mycursor.execute("""
CREATE TABLE IF NOT EXISTS hospital_details (
    Hospital_Id INT,
    Hospital_Name VARCHAR(50),
    Bed_count INT
)
""")

# Step 3: Insert data into hospital_details
hospital_data = [
    (1, "Janta", 200),
    (2, "Zydus", 500),
    (3, "Sal", 1000),
    (4, "Stirling", 1500)
]

mycursor.executemany(
    "INSERT INTO hospital_details VALUES (%s, %s, %s)",
    hospital_data
)

# Step 4: Create doctor_details table
mycursor.execute("""
CREATE TABLE IF NOT EXISTS doctor_details (
    Doctor_Id INT,
    Doctor_Name VARCHAR(50),
    Hospital_Id INT,
    Speciality VARCHAR(50),
    Salary INT,
    Experience INT
)
""")

# Step 5: Insert data into doctor_details
doctor_data = [
    (101, "Karan", 1, "Pediatric", 40000, 0),
    (102, "Naresh", 1, "Oncologist", 80000, 5),
    (103, "Hardik", 2, "Surgeon", 60000, 2),
    (104, "Vishal", 2, "Homeopathy", 50000, 1),
    (105, "Jay", 3, "Ayurvedic", 40000, 0),
    (106, "Deep", 3, "Physiotherapist", 70000, 4),
    (107, "Divyesh", 4, "Pediatric", 55000, 3),
    (108, "Arjun", 4, "Skin", 55000, 3)
]

mycursor.executemany(
    "INSERT INTO doctor_details VALUES (%s, %s, %s, %s, %s, %s)",
    doctor_data
)

# Step 6: Save changes
mydb.commit()

print("Tables created and data inserted successfully!")