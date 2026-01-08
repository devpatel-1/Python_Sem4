# Write a program to count number of digits, upper-case characters and lower-case characters from the string.

st = "Dev Patel 20 "

digits = 0
upper = 0
lower = 0

for ch in st:
    if ch >= '0' and ch <= '9':
        digits +=1
    elif ch >= 'A'and ch <= 'Z':
        upper += 1
    elif ch >= 'a' and ch <= 'z':
        lower += 1

print("Digits: ", digits)
print("Upper-case: ", upper)
print("Lower-case: ", lower)
