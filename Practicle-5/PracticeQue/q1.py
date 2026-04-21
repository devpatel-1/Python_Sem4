# Step 1: Create dictionary
students = {
    "Amit": [85, 78],
    "Riya": [92, 88],
    "Karan": [70, 65],
    "Neha": [80, 90]
}

print("Initial Dictionary:")
print(students)

# Step 2: Add new student
students["Rahul"] = [88, 82]

print("\nAfter Adding New Student:")
print(students)

# Step 3: Remove students with attendance below 75%
for name in list(students.keys()):
    if students[name][0] < 75:
        del students[name]

print("\nAfter Removing Students with Attendance < 75%:")
print(students)

# Step 4: Print students who scored above 80 marks
print("\nStudents scoring above 80 marks:")
for name, data in students.items():
    if data[1] > 80:
        print(name)