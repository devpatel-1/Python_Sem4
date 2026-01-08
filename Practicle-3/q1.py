# Write a program to check if number is Armstrong.

num = input("Enter number to check : ")
l = len(num)
num = int(num)

temp = num

sum = 0

while(temp != 0):
    sum = sum + (temp % 10) ** l
    temp = temp//10 
if(sum == num):
    print(f"Number {num} is a armstrong")
else:
    print(f"Num {num} is not a armstrong")
