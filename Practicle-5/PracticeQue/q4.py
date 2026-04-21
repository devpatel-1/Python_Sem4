# Step 1: Create contact dictionary
contacts = {
    "Amit": ["9876543210", "amit@gmail.com", "Delhi"],
    "Riya": ["9123456780", "riya@yahoo.com", "Mumbai"],
    "Karan": ["9988776655", "karan.gmail.com", "Delhi"],
    "Neha": ["9012345678", "neha@gmail.com", "Ahmedabad"]
}

print("Initial Contacts:")
print(contacts)

# Step 2: Find contacts from a specific city
city = "Delhi"
print("\nContacts from city:", city)

for name, details in contacts.items():
    if details[2] == city:
        print(name)

# Step 3: Update contact details
contacts["Riya"] = ["9123456780", "riya_new@gmail.com", "Mumbai"]

print("\nAfter Updating Riya's Details:")
print(contacts)

# Step 4: Remove contacts without '@' in email
for name in list(contacts.keys()):
    if '@' not in contacts[name][1]:
        del contacts[name]

print("\nAfter Removing Invalid Email Contacts:")
print(contacts)

# Step 5: Print contacts whose names start with a given character
ch = 'A'
print("\nContacts starting with letter:", ch)

for name in contacts:
    if name.startswith(ch):
        print(name)