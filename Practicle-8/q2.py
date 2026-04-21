#  Write a program to create class Student with following attributes: instance variables enrollment_no, name and branch; instance methods get_value() and print_value(); class variable cnt; static method show(). Variable cnt counts number of instances created and show() method displays value of cnt.


class Student:

    # class variable 
    cnt = 0

    # constructor
    def __init__(self):
        Student.cnt += 1
        
    # Instance method to get values
    def get_value(self):
        self.enrollment_no = input("Enter enrollment number: ")
        self.name = input("Enter name: ")
        self.branch = input("Enter branch: ")

    # Instance method to print values
    def print_value(self):
        print("Enrollment No: ", self.enrollment_no)
        print("Name: ", self.name)
        print("Branch: ", self.branch)
        print("---------------------------")

    @staticmethod
    def show():
        print("Total Students: ", Student.cnt)

# Create objects
s1 = Student()
s1.get_value()

s2 = Student()
s2.get_value()

s4 = Student()
s4.get_value()

# Display values
s1.print_value()
s2.print_value()
s4.print_value()

# Show count
Student.show()