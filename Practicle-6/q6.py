# WAP a function called powers(n) that prints out the first 5 powers of a given number. 
# Eg. >>> powers(6) 
# The first 5 powers of 6 are: 1 6 36 216 1296

def powers(n):
    print("The first 5 powers of", n, "are: ")

    for i in range(5):
        print(n ** i, end=" ")

powers(7)
