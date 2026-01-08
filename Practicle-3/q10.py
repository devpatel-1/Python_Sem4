# Write a python program to check if the substring is present in a given string.

s = input("Enter main string: ")
sub = input("Enter substring: ")

found = False

for i in range(len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub:
        found = True
        break

if found:
    print("Substring is present")
else:
    print("Substring is not present")

