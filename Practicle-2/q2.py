# Write a python program which takes student information such as Name, Enrollment Number, Branch, Age, Email and Mobile number from user and print as following:

#  “===========================” 
# Your Name
# Your Enrollment No. 
# Branch: CE/IT 
# Age:XX years
# Email:your mail ID 
# Mobile No: your No. 
# “===========================” 


print ("===========================")
name = input("Enter your name: ")
enno = input("Enter your Enrollment Number: ")
branch = input("Enter your Branch (CE/IT): ")
age = input("Enter your Age: ")
email = input("Enter Email ID: ")
mobile = input("Enter Mobile Number: ")


print("===========================")
print(name)
print("Enrollment No.:", enno)
print("Branch:", branch)
print("Age:", age, "years")
print("Email:", email)
print("Mobile No.:", mobile)
print("===========================")
