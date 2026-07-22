# Create a dictionary to store product names and their prices
inventory = {"Apple": 1.50, "Banana": 0.75, "Milk": 3.20}

# 1. Add a new product
inventory["Bread"] = 2.50

# 2. Display all products
print("--- Product List ---")
for product, price in inventory.items():
    print(f"{product} -> ${price}")

# 3. Look up a product's price
item = "Milk"
if item in inventory:
    print(f"\nPrice of {item}: ${inventory[item]}")

# 4. Calculate total price of all items
total_price = sum(inventory.values())
print(f"Total inventory value: ${total_price}")