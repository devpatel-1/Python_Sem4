# Print the names which contain the character 'a' from the dictionary containing 2 lists of male and female students given below.
# {"male": ["Tom", "Charlie", "Harry", "Frank"],
#     "female":["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"] }


students = {
    "male": ["Tom", "Charlie", "Harry", "Frank"],
    "female": ["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
}

print("Names containing 'a': ")

for group in students:
    for name in students[group]:
        if 'a' in name.lower():
            print(name)

            