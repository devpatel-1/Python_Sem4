# Create and initialize tuple
courses = ("JAVA", "PHP", "C#", "Android")

print("Original Tuple:", courses)

# Convert tuple to list
temp_list = list(courses)

# Insert items at 3rd position (index 2)
temp_list.insert(2, "HTML")
temp_list.insert(3, "Python")

# Convert list back to tuple
courses = tuple(temp_list)

print("Updated Tuple:", courses)

