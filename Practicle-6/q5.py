# Write a function to add two lists of the same length term-by-term & return new list 
# Eg.: A=listAdd([1,2,3],[1,2,3] )
# print (A) Will print [2,4,6].

def listAdd(a, b):
    result = []

    for i in range(len(a)):
        result.append(a[i] + b[i])

    return result

A = listAdd([1, 2, 3], [1, 2, 3])

print(A)