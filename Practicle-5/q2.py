# Using above created dictionary perform following operations
# 1)Write a code to print out the value of a, d, and c.
# 2) Calculate the sum of the value of a,b,c,d and print it.
# 3)Add a new key, value pair (e,5) to the dictionary and print dictionary.



d = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}

print("Value of a: ", d['a'])
print("Value of b: ", d['b'])
print("Value of c: ", d['c'])

total = d['a'] + d['b'] + d['c'] + d['d']
print("Sum of values: ", total)

d['e'] = 5
print("Updated dictionary: ", d)