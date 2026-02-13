# Given list of words
words = ["Python", "Java", "SQL", "HTML", "Android", "AI"]

print("Original Words:", words)

# 1. List containing length of each word
lengths = []
for w in words:
    lengths.append(len(w))

print("Length of each word:", lengths)

# 2. List of words with odd number of characters
odd_words = []
for w in words:
    if len(w) % 2 != 0:
        odd_words.append(w)

print("Words with odd length:", odd_words)

# 3. List of words starting with vowels
vowel_words = []
for w in words:
    ch = w[0]
    if ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U' or \
       ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        vowel_words.append(w)

print("Words starting with vowels:", vowel_words)