# Step 1: Create shopping cart
cart = {
    'apple': [50, 2],     # [price_per_unit, quantity]
    'mango': [80, 1],
    'banana': [40, 3]
}

print("Initial Cart:")
print(cart)

# Step 2: Calculate total bill
total = 0
for item in cart:
    price = cart[item][0]
    qty = cart[item][1]
    total = total + (price * qty)

print("\nTotal Bill:", total)

# Step 3: Update quantity
cart['apple'][1] = 4

print("\nAfter Updating Quantity of Apple:")
print(cart)

# Step 4: Add new item
cart['orange'] = [60, 2]

print("\nAfter Adding New Item:")
print(cart)

# Step 5: Remove items with quantity 0
cart['mango'][1] = 0

for item in list(cart.keys()):
    if cart[item][1] == 0:
        del cart[item]

print("\nAfter Removing Items with Quantity 0:")
print(cart)