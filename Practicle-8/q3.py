# Write a program to overload ** (exponential) operator.


class Power:

    def __init__(self, value):
        self.value = value

    def __pow__(self, other):
        return self.value ** other.value
    

a = Power(3)
b = Power(8)

result = a ** b

print("Result: ", result)