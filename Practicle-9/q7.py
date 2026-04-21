import sqlite3

# Step 1: Create in-memory database
conn = sqlite3.connect(":memory:")

print("In-memory database created!")

# Step 2: Create cursor
cursor = conn.cursor()

# Step 3: Create table
cursor.execute("""
CREATE TABLE student (
    id INTEGER,
    name TEXT
)
""")

print("Table created successfully!")

# Step 4: Insert data (optional)
cursor.execute("INSERT INTO student VALUES (1, 'Dev')")

# Step 5: Fetch data
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()

print("\nData in table:")
for row in rows:
    print(row)

# Step 6: Close connection
conn.close()