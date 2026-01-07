# Write a Python program that takes basic product information (product name, price, quantity, manufacturer) from the user and displays it in a formatted catalog-style output using proper spacing and alignment.

print("----------- PRODUCT CATALOG -----------")

name = input("Enter Product Name: ")
price = float(input("Enter Price: "))
qty = int(input("Enter Quntity: "))
mfg = input("Enter Manufacturer: ")

print("\n------------- PRODUCT DETAILS -------------")
print("{:<15} : {}".format("Product Name", name))
print("{:<15} : Rs.{:.2f}".format("Price", price))
print("{:<15} : {}".format("Quantity", qty))
print("{:<15} : {}".format("Manufacturer", mfg))
print("-------------------------------------")



# Great question Dev — this part is all about formatted output (very important for practical marks).

# Let’s understand it line by line in very easy words 👇

# ⸻

# 1️⃣

# print("\n---------- PRODUCT DETAILS ----------")

# 	•	\n → gives a new line (blank line before heading)
# 	•	Then prints a heading line.

# ⸻

# 2️⃣

# print("{:<15} : {}".format("Product Name", name))

# This prints:

# Product Name    : Laptop

# Part	Meaning
# {:<15}	Left align text in 15 spaces width
# "Product Name"	goes into {:<15}
# {}	prints value of name variable
# :	just printed as separator


# ⸻

# 3️⃣

# print("{:<15} : Rs.{:.2f}".format("Price", price))

# Example output:

# Price           : Rs.55000.00

# Part	Meaning
# {:<15}	left aligned label
# Rs.	rupees symbol text
# {:.2f}	float number with 2 decimal places


# ⸻

# 4️⃣

# print("{:<15} : {}".format("Quantity", qty))

# Prints quantity properly aligned:

# Quantity        : 2


# ⸻

# 5️⃣

# print("{:<15} : {}".format("Manufacturer", mfg))

# Prints:

# Manufacturer    : HP


# ⸻

# 6️⃣

# print("-------------------------------------")

# Just prints a line for design.

# ⸻

# 🧠 Why we use {:<15}?

# To make all labels start from same position — it makes output look clean like a real bill / catalog.

# ⸻

# 🎯 Viva Line

# {:<15} is used for left alignment with fixed width formatting.