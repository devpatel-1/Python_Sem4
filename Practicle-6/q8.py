# Write a Python program to sort a list of dictionaries using lambda function. The program should sort the list based on the 'age' key in each dictionary.


people = [
    {"name" : "Dev", "age" : 20},
    {"name" : "Alice", "age" : 18},
    {"name" : "Raj", "age" : 22}
]

people.sort(key=lambda x: x['age'])

print("Sorted List: ", people)