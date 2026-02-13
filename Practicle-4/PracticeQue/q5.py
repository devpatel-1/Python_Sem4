# Given lists
cities = ['Ahmedabad', 'Mumbai', 'Delhi', 'Bangalore']
codes = ['AMD', 'BOM', 'DEL', 'BLR']

print("Original Cities List:", cities)
print("City Codes List:", codes)

# 1. Create comma-separated string from cities list
city_string = ""
for i in range(len(cities)):
    city_string = city_string + cities[i]
    if i != len(cities) - 1:
        city_string = city_string + ","

print("\nComma-separated String:", city_string)

# 2. Split string back into a new list
new_cities = city_string.split(",")

print("New Cities List after split:", new_cities)

# 3. Compare original and new list
if cities == new_cities:
    print("Original list and new list are SAME")
else:
    print("Original list and new list are DIFFERENT")

# 4. Create tuple combining city and its code
city_code_tuple = []
for i in range(len(cities)):
    city_code_tuple.append((cities[i], codes[i]))

city_code_tuple = tuple(city_code_tuple)

print("\nTuple of City and Code:", city_code_tuple)