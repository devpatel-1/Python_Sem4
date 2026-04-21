# WAP to sort element in list 
# 1. In same list 
# 2. Create sorted copy of original list & print both.
# 3. Sort without any built-in function


lst = [5, 2, 9, 1, 7]

print("Original list: ", lst)

lst.sort()
print("After sort(): ", lst)

lst = [5, 2, 9, 1, 7]

new_lst = sorted(lst)
print("Originl List:", lst)
print("Sorted Copy: ", new_lst)

lst2 = [5, 2, 9, 1, 7]

n = len(lst2)

for i in range(n):
    for j in range(0, n-i-1):
        if lst2[j] > lst2[j+1]:
            lst2[j], lst2[j+1] = lst2[j+1], lst2[j]

print("Sorted without built in function: ", lst2)