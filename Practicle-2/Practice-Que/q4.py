# Write a program to take user's first name, last name, and birth year, then create an email ID and username following this pattern:
# Email: firstname.lastname@uvpce.edu.in
# Username: lastname_firstnameYY (YY is last 2 digits of birth year)


fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
byear = input("Enter your birth year (YYYY): ")

email = fname.lower() + "." + lname.lower() + "@uvpce.edu.in"
yy = byear[-2:]  # Last 2 digits of birth year
username = lname.lower() + "_" + fname.lower() +yy

print("\n------ GENERATED DETAILS ------")
print("Email ID  :", email)
print("Username  :", username)
print("-------------------------------")