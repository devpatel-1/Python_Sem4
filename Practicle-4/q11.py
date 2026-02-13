import re

# Input mobile number
mobile = input("Enter mobile number: ")

# Regular expression for valid mobile number
pattern = r'^[6-9]\d{9}$'

# Check validity
if re.match(pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")