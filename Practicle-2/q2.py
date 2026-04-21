# Write a python program which takes student information such as Name, Enrollment Number, Branch, Age, Email and Mobile number from user and print as following:

#  “===========================” 
# Your Name
# Your Enrollment No. 
# Branch: CE/IT 
# Age:XX years
# Email:your mail ID 
# Mobile No: your No. 
# “===========================” 


name = input("Entey your name: ")
enrollment = input("Enter your enrollment number: ")
branch = input("Enter your branch: ")
age = input("Enter your age: ")
email = input("Enter your email: ")
mobile = input("Enter your mobile number: ")


print("===========================")
print(name)
print("Enrollment No. :", enrollment)
print("Branch:", branch)
print("Age:", age, "years")
print("Email:", email)
print("Mobile No:", mobile)
print("===========================")
