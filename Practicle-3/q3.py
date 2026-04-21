# Create a program that will print out words that start with 's' from the below given statement.


statement = input("Enter a sentence: ")

words = statement.split()

for word in words:
    if word.lower().startswith('s'):
        print(word)

