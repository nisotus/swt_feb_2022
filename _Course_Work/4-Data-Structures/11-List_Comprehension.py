# So below is the usage of "map()" and "filter()" funcions that we just learned about
# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12)
# ]

# prices = list(map(lambda item:item[1], items))

# filtered = list(filter(lambda item:item[1] >= 10, items))

# print(prices)
# print(filtered)

# The map() and filter() functions are very useful in Python
# But they are often used by developers who came from functional programming background

# However, in Python we have another feature for achieving th same result
# And we do not have this feature in other programming languages

# This feature is called "COMPREHENSION"

# **** LIST COMPREHENSION ****
# [item[1] for item in items]
 # produces the same result as below:
# prices = list(map(lambda item:item[1], items))
# filtered = list(filter(lambda item:item[1] >= 10, items))

# *** Mapping a list into another list
# So let's store the result of our list comprehension in the variable "prices"
# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12)
# ]


# prices = [item[1] for item in items]
# print(prices)

# *** Filtering a list using list comprehension
# We can also filter items in a list using the list comprehension expression
# [expression for item in items]
# Now, what is the "expression" in this case?
# Well, in this case we don't want to map the list of items to the list of prices

# So in this case, our expression is simply the "item" itself
# We iterate over the list of items, we get each item
# and simply return the item

# However, we want to filter them
# So, we'll add an IF STATEMENT - "if item[1] >= 10"

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

filtered = [item for item in items if item[1] >= 10]
print(filtered)

prices = [item[1] for item in items]
print(prices)
