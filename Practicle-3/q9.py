# Write a python program to remove i’th character from string.

s = input("Enter a string: ")
i = int(input("Enter position to remove: "))

new_str = ""

for pos in range(len(s)):
    if pos != i:
        new_str = new_str + s[pos]

print("String after removing character:", new_str)