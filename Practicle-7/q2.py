# Write a Python program to combine each line from first file with the corresponding line in second file.


f1 = open("/Users/devpatelsm4/Desktop/Sem-4-Material/Python/Python/Practicle-7/file1.txt", "r")
f2 = open("/Users/devpatelsm4/Desktop/Sem-4-Material/Python/Python/Practicle-7/file2.txt", "r")

lines1 = f1.readlines()
lines2 = f2.readlines()

f1.close()
f2.close()

for l1, l2 in zip(lines1, lines2):
    print(l1.strip() + " " + l2.strip())