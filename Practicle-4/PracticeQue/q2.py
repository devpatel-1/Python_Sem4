# Initial lists
products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor']
prices = [45000, 890, 920, 15600]

print("Original Products:", products)
print("Original Prices:", prices)

# 1. Insert new product with price at position 2 (index 1)
products.insert(1, 'Printer')
prices.insert(1, 12000)

# 2. Remove product 'Mouse' and its corresponding price
index = products.index('Mouse')
products.pop(index)
prices.pop(index)

# 3. Update price of 'Monitor'
monitor_index = products.index('Monitor')
prices[monitor_index] = 18000

# 4. Display products with prices > 1000
print("\nProducts with price greater than 1000:")
for i in range(len(prices)):
    if prices[i] > 1000:
        print(products[i], "-", prices[i])