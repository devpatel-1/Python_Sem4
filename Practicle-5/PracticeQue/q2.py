# Step 1: Create library dictionary
books = {
    'Python': ['John Smith', 5, 'Programming'],
    'Digital Logic': ['Mike Ross', 3, 'Electronics'],
    'Data Science': ['Sarah Connor', 0, 'Analytics']
}

print("Initial Library Catalog:")
print(books)

# Step 2: Add a new book
books['AI Basics'] = ['Andrew Ng', 4, 'Programming']

print("\nAfter Adding New Book:")
print(books)

# Step 3: Update number of copies
books['Python'][1] = 7

print("\nAfter Updating Copies of Python Book:")
print(books)

# Step 4: Print books of a specific category
category = 'Programming'
print("\nBooks in category:", category)

for book, details in books.items():
    if details[2] == category:
        print(book)

# Step 5: Remove books with 0 copies
for book in list(books.keys()):
    if books[book][1] == 0:
        del books[book]

print("\nAfter Removing Books with 0 Copies:")
print(books)