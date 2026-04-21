# Write a program to check special number. (Number is equal to the sum of its divisors).

# Taking input
num = int(input("Enter a number: "))

sum_div = 0

# Finding divisors
for i in range(1, num):
    if num % i == 0:
        sum_div += i

# Checking special number
if sum_div == num:
    print("It is a Special Number")
else:
    print("It is NOT a Special Number")