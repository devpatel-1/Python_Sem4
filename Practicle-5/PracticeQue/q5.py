# Step 1: Create courses dictionary
courses = {
    'Python': ['Lab 1', 30, ['John', 'Mike']],
    'Java': ['Lab 2', 25, ['Sarah', 'Tom']],
    'Web Dev': ['Lab 3', 20, ['Alex']]
}

print("Initial Courses:")
print(courses)

# Step 2: Add a new course
courses['Data Science'] = ['Lab 4', 15, ['Emma', 'Noah', 'Liam', 'Olivia', 'Ava']]

print("\nAfter Adding New Course:")
print(courses)

# Step 3: Enroll a student in a course
course_name = 'Python'
student_name = 'David'

if course_name in courses:
    courses[course_name][2].append(student_name)

print("\nAfter Enrolling Student in Python Course:")
print(courses)

# Step 4: Remove courses with less than 5 students
for course in list(courses.keys()):
    if len(courses[course][2]) < 5:
        del courses[course]

print("\nAfter Removing Courses with Less Than 5 Students:")
print(courses)

# Step 5: Display available seats in each course
print("\nAvailable Seats in Each Course:")
for course, details in courses.items():
    max_capacity = details[1]
    enrolled = len(details[2])
    available_seats = max_capacity - enrolled
    print(course, ":", available_seats)