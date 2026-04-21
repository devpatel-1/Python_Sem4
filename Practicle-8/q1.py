# 1) Create a class Employee with data members: name, department and salary. Use constructor to initialize values and display() method for printing information of three employees.


class Employee:

    # Constructor
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    # Display method
    def display(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("-----------------------------")

e1 = Employee("Dev", "IT", 50000)
e2 = Employee("Rohit", "HR", 45000)     
e3 = Employee("Sita", "Finance", 60000)

e1.display()
e2.display()
e3.display()