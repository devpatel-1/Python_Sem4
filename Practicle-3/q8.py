# Write a python program to check if a string is a palindrome or not.

s = input("Enter a string: ")

rev = s[::-1]

if s == rev:
    print("The string is Palindrome")
else:
    print("The string is Not Palindrome")