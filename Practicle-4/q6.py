# Write a Python program which takes a list and returns a list with the elements "Shifted left by one position" so [1, 2, 3] yields [2, 3, 1].
# Example: [11, 12, 13] → [12, 13, 11]


lst = [11, 12, 13]

first = lst[0]

for i in range(len(lst) - 1):
    lst[i] = lst[i + 1]

lst[-1] = first

print("Shifted list: ", lst)