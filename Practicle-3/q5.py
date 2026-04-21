# Write a program to find the sum of digit of an input number using while loop.


num = int(input("Enter a number: "))

sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10

print("Sum of digits =", sum)