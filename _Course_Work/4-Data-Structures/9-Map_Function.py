# So below we have a list of items. Let us imagine we want to transform this list into a different shape
# Currently each item in the list is a TUPLE of two items
# Let's say we are only interested in the price of these items
# Meaning we want to transform this list to a list of only numbers = List of prices

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12)
# ]

# Below is a basic way to do this

# Define an empty list
# prices = []

# Iterate over the list of items
# for item in items:
#     prices.append(item[1])
    
# Now let's print the prices

# print(prices)

# With the FOR LOOP, we were able to transform or map the original list into a different list

# There is a BETTER WAY to do this
# Instead of using the FOR LOOP, we can use the "map()" function

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12)
# ]

# x = map(lambda item:item[1], items)
# for item in x:
#     print(item)

# print(x)
    
# The map() function take two parameters - "a function" and one or more "iterable"
# map(func, *iterables)

# We can use LIST function with map() function

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

prices = list(map(lambda item:item[1], items))
print(prices)

# ***This is how the map() function works***
# It takes a lambda function and applies it on every item of an iterable
