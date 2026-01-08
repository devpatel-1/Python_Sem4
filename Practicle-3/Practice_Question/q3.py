# Write a program that takes a string input and creates a new string by replacing:
# all vowels with '*'
# all digits with '#'
# all spaces with '_'
# Display both original and modified strings.

s = input("Enter a string: ")

new_str = ""

for ch in s:
    if ch in "aeiouAEIOU":
        new_str = new_str + "*"
    elif ch.isdigit():
        new_str = new_str + "#"
    elif ch == " ":
        new_str = new_str + "_"
    else:
        new_str = new_str + ch

print("Original string:", s)
print("Modified string:", new_str)