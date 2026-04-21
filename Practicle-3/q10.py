# Write a python program to check if the substring is present in a given string.


# Taking input
main_str = input("Enter main string: ")
sub_str = input("Enter substring: ")

# Checking substring
if sub_str in main_str:
    print("Substring is present")
else:
    print("Substring is NOT present")