# Filter the dictionary by removing all items with a value greater than 2.
#    d={“a”:1, “b”:2, “c”:3, “d”:4, “d”:5}


d = {'a': 1, 'b': 2, 'c': 3, 'd': 5}

filtered = {}

for key, value in d.items():
    if value <= 2:
        filtered[key] = value

print("Filtered dictionary: ", filtered)

