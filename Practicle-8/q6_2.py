class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class SportPerson(Person):
    def __init__(self, name, age, sport_name):
        Person.__init__(self, name, age)
        self.sport_name = sport_name


sp = SportPerson("Rohit", 22, "Football")

print("Name:", sp.name)
print("Age:", sp.age)
print("Sport:", sp.sport_name)