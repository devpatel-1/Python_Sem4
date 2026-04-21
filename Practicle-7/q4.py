# Write a Python program to write students information into csv file and read that details.


import csv

students = [
    ["Name", "Age", "Branch"],
    ["Dev", 20, "CE"],
    ["Raj", 19, "IT"],
    ["Amit", 21, "ME"]
]

file = open("/Users/devpatelsm4/Desktop/Sem-4-Material/Python/Python/Practicle-7/students.csv", "w", newline = "")
writer = csv.writer(file)

writer.writerows(students)

file.close()

print("Data written to CSV file.")

file = open("students.csv", "r")
reader = csv.reader(file)

print("Reading CSV file: ")
for row in reader:
    print(row)

file.close()