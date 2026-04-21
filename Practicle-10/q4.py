from tkinter import *
import sqlite3

# Create database
conn = sqlite3.connect("student.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    enrollment TEXT,
    name TEXT,
    gender TEXT,
    address TEXT,
    branch TEXT,
    mobile TEXT,
    email TEXT
)
""")
conn.commit()

# Function to insert data
def submit():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO students VALUES (?,?,?,?,?,?,?)", (
        entry_enroll.get(),
        entry_name.get(),
        gender.get(),
        text_address.get("1.0", END),
        branch.get(),
        entry_mobile.get(),
        entry_email.get()
    ))

    conn.commit()
    conn.close()

# Function to view data
def view():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()

# GUI Window
root = Tk()
root.title("Registration Page")
root.geometry("400x400")

# Variables
gender = StringVar()
branch = StringVar()

# Labels & Entries
Label(root, text="Enter Enrollment No:").grid(row=0, column=0)
entry_enroll = Entry(root)
entry_enroll.grid(row=0, column=1)

Label(root, text="Enter Name:").grid(row=1, column=0)
entry_name = Entry(root)
entry_name.grid(row=1, column=1)

Label(root, text="Select Gender:").grid(row=2, column=0)
Radiobutton(root, text="Male", variable=gender, value="Male").grid(row=2, column=1)
Radiobutton(root, text="Female", variable=gender, value="Female").grid(row=2, column=2)

Label(root, text="Enter Address:").grid(row=3, column=0)
text_address = Text(root, height=3, width=20)
text_address.grid(row=3, column=1)

Label(root, text="Select Branch:").grid(row=4, column=0)
OptionMenu(root, branch, "CSE", "IT", "ECE", "ME").grid(row=4, column=1)

Label(root, text="Enter Mobile:").grid(row=5, column=0)
entry_mobile = Entry(root)
entry_mobile.grid(row=5, column=1)

Label(root, text="Enter Email:").grid(row=6, column=0)
entry_email = Entry(root)
entry_email.grid(row=6, column=1)

# Buttons
Button(root, text="Submit", command=submit).grid(row=7, column=0, pady=10)
Button(root, text="View", command=view).grid(row=7, column=1)

# Run GUI
root.mainloop()