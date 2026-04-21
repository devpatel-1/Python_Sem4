# Write a program to create a regular expression which verifies whether given mobile number is valid or not.


import re

num = input("Enter a mobile number: ")

pattern = "^[6-9][0-9]{9}$"

if re.match(pattern, num):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")

