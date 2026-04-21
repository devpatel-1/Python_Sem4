# Write a Python program to read content from a file and display the word with maximum length.



file = open("/Users/devpatelsm4/Desktop/Sem-4-Material/Python/Python/Practicle-7/data.txt", "r")

text = file.read()

file.close()

words = text.split()

max_word = words[0]

for w in words:
    if len(w) > len(max_word):
        max_word = w

print("Word with maximum length: ", max_word)