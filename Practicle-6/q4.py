# Write a function to find the minimum and maximum value from argument list & return both minimum & maximum in tuple form. 

def find_min_max(*args):
    min_value = args[0]
    max_value = args[0]

    for i in args:
        if i < min_value:
            min_value = i
        if i > max_value:
            max_value = i

    return (min_value, max_value)

result = find_min_max(10, 4, 6, 7, 23)

print("Minimum and Maximum: ", result)