# Explain difference between insert, append and extend operations on list. Write a program to create and initialize a list with your name, enrollment number, age, branch and result. Perform insert, remove, update, append and extend operation on list.

data = ["Dev Patel", "123456", 20, "CE", "Pass"]

print("Original List:", data)

data.insert(2, "India")
print("After Insert:", data)

data.append("Python")
print("After Append:", data)

data.extend(["AI", "ML"])
print("After Extend:", data)

data[0] = "Dev P."
print("After Update:", data)

data.remove("Pass")
print("After Remove:", data)