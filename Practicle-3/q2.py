# Write a program to check special number. (Number is equal to the sum of its divisors).

n = input("Enter num to check that it is special or not : ")

sum = 0

n = int(n)

for i in range(1, n):
    if(n % i == 0): 
        sum = sum + i
if(sum == n):
    print(f"{n} is a special num")
else:
    print(f"{n} is not a special num")	