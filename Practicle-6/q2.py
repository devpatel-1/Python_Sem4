# Write a program to display all the prime numbers between 1 to n using function.


def print_primes(n):
    for num in range(2, n + 1):
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            print(num, end=" ")

n = int(input("Enter a number: "))

print("Prime numbers are: ")
print_primes(n)
