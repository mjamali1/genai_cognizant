print("Welcome to the Inventory Manager!")

# create inventory
inventory = { "dress": (5, 50.0), "hoodie": (10, 40.0)}

# display inventory
print("Current Inventory:")
for item, (quantity, price) in inventory.items():
    print("Item: ", item, ", Quantity: ", quantity, ", Price: $", price, sep="")
# step 2 

# adding an item 
inventory["tshirt"] = (15, 10.0)
print("Adding a new item: tshirt")

# removing an item
del inventory["hoodie"]
print("Removing an item: hoodie")

# updating an item
inventory["dress"] = (3, 50.0) 
print("Updating item: dress")

print("Updated Inventory:")
for item, (quantity, price) in inventory.items():
    print("Item: ", item, ", Quantity: ", quantity, ", Price: $", price, sep="")


# Step 4: Calculate Total Value
total_value = sum(quantity * price for quantity, price in inventory.values())
print("Total value of inventory: $", total_value)
