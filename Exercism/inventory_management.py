# 1. Create an inventory based on a list
# Implement the create_inventory() function that creates an "inventory" from a list of items.
# It should return a dict containing each item name paired with their respective quantity.

def create_inventory(list_of_products):
    my_dict = {}
    for item in list_of_products:
        my_dict[item] = list_of_products.count(item)
    return my_dict


# print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))

# 2. Add items from a list to an existing dictionary
# Implement the add_items() function that adds a list of items to an inventory:

def add_items(my_dict, list_of_products):
    for value in list_of_products:
        if value in my_dict:
            my_dict[value] += 1
        else:
            my_dict[value] = 1
    return my_dict


# print(add_items({"coal":1}, ["wood", "iron", "coal", "wood", "goods"]))

# 3. Decrement items from the inventory
# Implement the decrement_items(<items>) function that takes a list of items. The function should remove one
# from the available count in the inventory for each time an item appears on the list:

def decrement_items(my_dict, list_of_products):
    for value in list_of_products:
        if my_dict[value] != 0:
            my_dict[value] -= 1
    return my_dict


# print(decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron", "diamond"]))

# 4. Remove an item entirely from the inventory
# Implement the remove_item(<inventory>, <item>) function that removes an item and its count entirely from
# an inventory:

def remove_item(inventory, item):
    inventory.pop(item,"")
    return inventory

# print(remove_item({"coal":2, "wood":1, "diamond":2}, "coal"))

# 5. Return the inventory content
# Implement the list_inventory() function that takes an inventory and returns a list of (item, quantity) tuples.
# The list should only include the available items (with a quantity greater than zero):

def list_inventory(inventory):
    my_list = []
    for item in inventory:
        if inventory[item] != 0:
            x = (item, inventory[item])
            my_list.append(x)
    return my_list

# print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))