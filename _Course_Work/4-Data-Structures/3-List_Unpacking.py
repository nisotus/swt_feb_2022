# There are times when you want to get individual ITEMS in list and assign them to VARIABLES
# Below is an example:

numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[2]

# LIST UNPACKING

# So we can unpack the list - "numbers = [1, 2, 3]" into multiple variables

# How to do this?

# We define our variables seperated by commas and set them to the list
numbers = [1, 2, 3]
first, second, third = numbers

# This will not work
# first, second = numbers

# So what if we have a list like below and we only care about the first two items
numbers = [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4]

# How to handle this?
# We can get the first and second and then pack the rest inside of a separate list called "*other"
# numbers = [1, 2, 3, 4, 4, 4, 4, 4, 4, 4]
# first, second, *other = numbers
# print(first)
# print(second)
# print(other)

# So in the example above we have both UNPACKING and PACKING

# Just like in FUNCTIONS, when we prefix a parameter with as asterisk(*),
# Python will get all the arbitrary arguments and pack them into a list

# This is exactly what is happening with - first, second, *other = numbers

# **********************************
# What if we care only about the first and the last item?
# How do we do this?

# numbers = [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 6, 7, 8]
# first, *other, last = numbers
# print(first)
# print(other)
# print(last)

#*************************
numbers = [1, 2, 3, 4]
first, another, *other, second, last = numbers
print(first)
print(another)
print(other)
print(second)
print(last)
