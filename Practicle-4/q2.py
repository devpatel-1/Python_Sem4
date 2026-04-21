# Write a program to search an element, find maximum & minimum value from the list. 
# 1. Using inbuilt function 
# 2. Using for loop


lst = [10, 5, 20, 8, 15]

x = int(input("Enter element to search: "))

if x in lst:
    print("Element found !!")
else:
    print("Element not found")

print("Max value:", max(lst))
print("Min value:", min(lst))