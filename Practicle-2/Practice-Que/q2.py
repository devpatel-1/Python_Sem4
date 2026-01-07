# Write a Python program that takes a student's marks in 5 subjects (out of 100) and calculates their percentage and grade (A: ≥90%, B: ≥80%, C: ≥70%, D: ≥60%, F: <60%). Display the results in a formatted output.


print("----------- STUDENT RESULT -----------")

s1 = float(input("Enter marks for Subject 1: "))
s2 = float(input("Enter marks of Subject 2: "))
s3 = float(input("Enter marks of Subject 3: "))
s4 = float(input("Enter marks of Subject 4: "))
s5 = float(input("Enter marks of Subject 5: "))

total = s1 + s2  + s3 + s4 + s5
percentage = (total / 500) * 100

if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
else:
    grade = 'F'


print("\n------ RESULT ------")
print("Total Marks   :", total)
print("Percentage    : {:.2f}%".format(percentage))
print("Grade         :", grade)
print("--------------------")