# Write a program to perform addition of two numbers using user defined function.

def add(a, b):
    return a + b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

result = add(x, y)

print("Sum = ", result)