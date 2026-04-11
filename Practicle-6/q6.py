
def power(n):
    print("The first 5 powers of number are: ")

    for i in range(5):
        print(n**i, end = " ")

num = int(input("Enter a number: "))

power(num)