class Vehicle:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"

    # method overloading (using default argument)
    def calculate_price(self, base_price=0):
        return base_price


class Car(Vehicle):

    def __init__(self, brand, model, year, seats, fuel_type):
        super().__init__(brand, model, year)
        self.seats = seats
        self.fuel_type = fuel_type

    def __str__(self):
        return super().__str__() + f", Seats: {self.seats}, Fuel: {self.fuel_type}"

    def calculate_price(self, base_price, tax=50000):
        return base_price + tax


class Bike(Vehicle):

    def __init__(self, brand, model, year, engine_cc):
        super().__init__(brand, model, year)
        self.engine_cc = engine_cc

    def __str__(self):
        return super().__str__() + f", Engine: {self.engine_cc}cc"

    def calculate_price(self, base_price, tax=20000):
        return base_price + tax


# Creating objects
car1 = Car("Toyota", "Camry", 2023, 5, "Petrol")
bike1 = Bike("Yamaha", "R15", 2022, 155)

# Display details
print(car1)
print("Car Price:", car1.calculate_price(2000000))

print()

print(bike1)
print("Bike Price:", bike1.calculate_price(150000))