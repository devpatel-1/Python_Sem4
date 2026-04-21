from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    # Operator overloading for comparing area
    def __gt__(self, other):
        return self.area() > other.area()


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle with radius {self.radius}"

    def __repr__(self):
        return f"Circle({self.radius})"

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Rectangle {self.length} x {self.width}"

    def __repr__(self):
        return f"Rectangle({self.length},{self.width})"

    @classmethod
    def from_square(cls, side):
        return cls(side, side)


class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def __str__(self):
        return f"Triangle sides {self.a},{self.b},{self.c}"

    def __repr__(self):
        return f"Triangle({self.a},{self.b},{self.c})"


# Creating objects using class methods
c = Circle.from_diameter(10)
r = Rectangle.from_square(5)
t = Triangle(3, 4, 5)

print(c)
print(r)
print(t)

print("Circle Area:", c.area())
print("Rectangle Area:", r.area())

# Comparing shapes
print("Circle > Rectangle:", c > r)