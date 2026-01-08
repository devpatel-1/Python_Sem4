# Write a program that takes a string containing both words and numbers (e.g., 'I have 2 cars and 3 bikes'). Extract all numbers, find their sum, and replace each number in the original string with its square. Display:
# Sum of all numbers
# Modified string (e.g., 'I have 4 cars and 9 bikes')

s = input("Enter a string: ")

words = s.split()
total = 0

for i in range(len(words)):
    if words[i].isdigit():
        num = int(words[i])
        total = total + num
        words[i] = str(num * num)

new_string = " ".join(words)

print("Sum of all numbers:", total)
print("Modified string:", new_string)