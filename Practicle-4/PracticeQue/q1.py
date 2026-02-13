# Given list of student scores
scores = [85, 92, 78, 65, 90, 76, 88, 79]

print("Original Scores:", scores)

# 1. Create a new list with scores above 80
above_80 = []
for s in scores:
    if s > 80:
        above_80.append(s)

print("Scores above 80:", above_80)

# 2. Find average score using for loop
total = 0
count = 0

for s in scores:
    total += s
    count += 1

average = total / count
print("Average Score:", average)

# 3. Sort scores in descending order (without built-in functions)
n = len(scores)

for i in range(n):
    for j in range(i + 1, n):
        if scores[i] < scores[j]:
            scores[i], scores[j] = scores[j], scores[i]

print("Scores in Descending Order:", scores)