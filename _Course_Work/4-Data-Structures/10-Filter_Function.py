# The filter function is another scenario for using a lambda function
# So we have our list of items, let's say we want to filter this list
# and only get the items with price greater than or equal to 10 Dollars

# *** Solution 1

# One basic way is to define an empty list, then we iterate over the list
# For each item, we get the price.
# If the price matches our criteria, we add it to the empty list

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

price = []

for item in items:
    if item >= 10:
        price.append(item)

print(price)

# ***********************

# But a better approach is to use the built-in filter() function
# The filter() function taks two parameters "a function" and an "iterable"

# So if we apply the filter() function on each item of the iterable
# If the item matches some criteria, it would return the match item

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12)
# ]

# filtered = list(filter(lambda item:item[1] >= 10, items))
# print(filtered)
