# Write a Python program to read first n lines of a file.


n = int(input("Enter number of lines to read: "))

file = open("/Users/devpatelsm4/Desktop/Sem-4-Material/Python/Python/Practicle-7/data1.txt", "r")

for i in range(n):
    line = file.readline()
    print(line.strip())

file.close()