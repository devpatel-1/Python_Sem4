# Write a program to generate Fibonacci series up to n terms where each number contains exactly 3 digits. For example, if a Fibonacci number is 89, display it as 089. If it exceeds 999, don't display it.

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    if a > 999:
        break

    if a < 10:
        print("00" + str(a))
    elif a < 100:
        print("0" + str(a))
    else:
        print(a)

    c = a + b
    a = b
    b = c