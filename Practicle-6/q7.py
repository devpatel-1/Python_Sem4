# Write a Python program to filter a list of integers using lambda function. The program should filter even numbers from a given list.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = list(filter(lambda x: x % 2 == 0, lst))

print("Even numbers: ", even)