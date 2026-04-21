# Write a python program to check if a string is a palindrome or not.

text = input("Enter a string: ")

if text == text[::-1]:
    print("It is a Palindrome")
else:
    print("It is NOT a Palindrome")

    