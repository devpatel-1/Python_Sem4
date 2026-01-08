# Write a program to find the sum of digit of an input number using while loop.


  
num = int(input("Enter the number: "))
# l = len(num)
temp = num
  
sum = 0
  
while temp != 0: 
      sum = sum + (temp % 10)
      temp = temp // 10
  
print(sum)
