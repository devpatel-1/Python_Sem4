class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class SportPerson(Person):
    def __init__(self, name, age, sport_name):
        super().__init__(name, age)
        self.sport_name = sport_name


sp = SportPerson("Rahul", 20, "Cricket")

print("Name:", sp.name)
print("Age:", sp.age)
print("Sport:", sp.sport_name)