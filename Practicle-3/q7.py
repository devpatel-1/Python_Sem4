# Write a program to count number of digits, upper-case characters and lower-case characters from the string.


text = input("Enter a string: ")

digits = 0
upper = 0
lower = 0


for ch in text:
    if ch.isdigit():
        digits += 1
    elif ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1


print("Digits:", digits)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
