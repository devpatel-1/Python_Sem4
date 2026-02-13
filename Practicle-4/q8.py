# Create and initialize a tuple
my_tuple = (10, 20, 30, 40, 50)

print("Original Tuple:", my_tuple)

# Convert tuple to list
temp_list = list(my_tuple)

# Remove 3rd element (index 2)
temp_list.pop(2)

# Convert list back to tuple
my_tuple = tuple(temp_list)

print("Tuple after removing 3rd element:", my_tuple)