
# Read about LAMBDA functions and you will discuss in class what you understand
# Also use LAMBDA functions to implement the code below:

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
    ("Product4", 1),
    ("Product6", 102),
    ("Product5", 3), 
    ("Product10", 3)   
]

# def sort_item(item):
#     return item[1]

# items.sort(key=sort_item)
# print(items)

items.sort(key=lambda item:item[1])
print(items)