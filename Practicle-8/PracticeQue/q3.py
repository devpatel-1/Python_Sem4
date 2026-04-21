from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @abstractmethod
    def calculate_performance(self):
        pass


class Student(Person):

    def __init__(self, name, age, roll_no, course):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        self.course = course

    def calculate_performance(self):
        print("Student performance based on marks")


class Faculty(Person):

    def __init__(self, name, age, department, salary):
        Person.__init__(self, name, age)
        self.department = department
        self.salary = salary

    def calculate_performance(self):
        print("Faculty performance based on teaching")


class TeachingAssistant(Student, Faculty):

    def __init__(self, name, age, roll_no, course, department, salary):
        Student.__init__(self, name, age, roll_no, course)
        Faculty.__init__(self, name, age, department, salary)

    def calculate_performance(self):
        print("TA performance based on study and teaching")


s = Student("Rahul", 20, 101, "BCA")
f = Faculty("Dr Sharma", 45, "Computer", 60000)
ta = TeachingAssistant("Amit", 24, 201, "MCA", "Computer", 20000)

s.calculate_performance()
f.calculate_performance()
ta.calculate_performance()