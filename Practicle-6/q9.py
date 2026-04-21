# Write a Python program to execute a function on each element of a list using lambda function. The program should calculate square of all numbers.


lst = [1, 2, 3, 4]

squares = list(map(lambda x: x ** 2, lst))

print("Squares: ", squares)