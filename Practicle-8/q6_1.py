# Class Person with attributes- name and age is inherited by class SportPerson with attribute sport_name. Use appropriate __init__() method for both classes. Call parent __init__() method from child __init__() method with the help of  (A) super() method (B) parent class name.


class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

class SportPerson(Person):

    def __init__(self, name, age, sport_name):
        super().__init__(name, age)
        self.sport_name = sport_name
    
    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Sport: ", self.sport_name)

s1 = SportPerson("Dev", 25, "F1")
s1.display()