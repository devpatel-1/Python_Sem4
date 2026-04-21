# Write a python program to count odd numbers from given three numbers and display maximum odd number.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

odd_numbers = []

if a % 2 != 0:
    odd_numbers.append(a)
if b % 2 != 0:
    odd_numbers.append(b)
if c % 2 != 0:
    odd_numbers.append(c)

print(f"\nOdd count: {len(odd_numbers)}")

if len(odd_numbers) > 0:
    print(f"Maximum odd number: {max(odd_numbers)}")
else:
    print("No odd numbers found!")