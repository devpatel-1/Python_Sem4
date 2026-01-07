# Write a python program to count odd numbers from given three numbers and display maximum odd number.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

count = 0
max_odd = None

if a % 2 != 0:
    count += 1
    max_odd = a

if b % 2 != 0:
    count += 1
    if max_odd is None or b > max_odd:
        max_odd = b

if c % 2 != 0:
    count += 1
    if max_odd is None or c > max_odd:
        max_odd = c

print("Total Odd Numbers =", count)

if count > 0:
    print("Maximum Odd Number =", max_odd)
else:
    print("No odd numbers found.")