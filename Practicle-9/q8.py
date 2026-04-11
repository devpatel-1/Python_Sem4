import sqlite3

# Step 1: Connect to database (creates file demo.db)
conn = sqlite3.connect("demo.db")

print("Database connected!")

# Step 2: Create cursor
cursor = conn.cursor()

# Step 3: Execute multiple queries using executescript()
cursor.executescript("""
CREATE TABLE IF NOT EXISTS hospital_details (
    Hospital_Id INTEGER,
    Hospital_Name TEXT,
    Bed_count INTEGER
);

CREATE TABLE IF NOT EXISTS doctor_details (
    Doctor_Id INTEGER,
    Doctor_Name TEXT,
    Hospital_Id INTEGER,
    Speciality TEXT,
    Salary INTEGER,
    Experience INTEGER
);

INSERT INTO hospital_details VALUES (1, 'Janta', 200);
INSERT INTO hospital_details VALUES (2, 'Zydus', 500);

INSERT INTO doctor_details VALUES (101, 'Karan', 1, 'Pediatric', 40000, 0);
INSERT INTO doctor_details VALUES (102, 'Naresh', 1, 'Oncologist', 80000, 5);
""")

# Step 4: Save changes
conn.commit()

print("Tables created and data inserted using executescript!")

# Step 5: Display data
cursor.execute("SELECT * FROM doctor_details")
rows = cursor.fetchall()

print("\nDoctor Details:")
for row in rows:
    print(row)

# Step 6: Close connection
conn.close()

