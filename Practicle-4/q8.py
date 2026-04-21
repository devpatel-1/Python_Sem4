# Write a program to create and initialize the tuple. Also remove 3rd element from tuple.

t = ("Dev", 12345, 20, "CE", "Pass")

print("Original Tuple: ", t)

temp = list(t)
temp.pop(2)

t = tuple(temp)

print("Updated Tuple: ", t)
