# Write a python program which shows the effect of mutability.

a = [1, 2, 3]

b = a

b.append(4)

print("List a: ", a)
print("List b: ", b)