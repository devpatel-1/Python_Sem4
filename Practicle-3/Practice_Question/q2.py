# Create a program that takes a sentence as input and performs the following operations:
# Count total words
# Display words containing exactly 5 characters
# Print the position of each vowel in the sentence

s = input("Enter a sentence: ")

words = s.split()

# Count total words
print("Total words:", len(words))

# Display words with exactly 5 characters
print("Words with exactly 5 characters:")
for w in words:
    if len(w) == 5:
        print(w)

# Print position of vowels
print("Position of vowels:")
pos = 1
for ch in s:
    if ch in "aeiouAEIOU":
        print(ch, "at position", pos)
    pos = pos + 1