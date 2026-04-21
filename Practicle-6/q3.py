# Write a user defined function to sort a List. 

def sort_list(lst):
    n = len(lst)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst

lst = [5, 2, 9, 1, 7]

sorted_list = sort_list(lst)

print("Sorted List: ", sorted_list)


