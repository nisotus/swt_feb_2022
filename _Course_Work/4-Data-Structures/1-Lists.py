# In this section we are going to look at the built-in data structures in Python
# Which are extremely important when building real world applications
# We will be looking at:

# LISTS
# TUPLES
# SETS
# DICTIONARIES

# List
[]

# Tuple
()

# Set
{}

# Dictionary
{}

# Example list of strings
letters = ["a", "b", "c", "d"]

# Example list of numbers
numbers = [1, 2, 3, 4]

# Example list of booleans
booleans = [True, False, True, False]

# We can have a list of lists which we call a MATRIX. A matrix is a two dimensional list
matrix1 = [[0, 1], [2, 3]]
matrix2 = [["a", "b"], ["c", "d"], ["e", "f"]]


# Small Exercise**********************
# I want you to print 100 zeros (0...) to the terminal
# zero = "0"
# zeros1 = zero * 100
# print(zeros1)

# Using the the "*" operator, we can repeat the item in a list
# zeros2 = [0] * 200
# print(zeros2)

# Similarly we can use the "+" operator to concatenate multiple lists
letters = ["a", "b", "c", "d"]
zeros = [0] * 10
combine = zeros + letters
print(combine)

# If you want to have a list of numbers from 0 to 20 and you don't want to type all of these by hand
# There is a way to do this using the "list()" function.
# The "list()" function takes an iterable as an argument

# So we can pass an iterable to the "list()" function and convert the iterable to a list
# The "range()" function returns a "range" object that is iterable - meaning we can iterate or loop over it
# So we can pass the "range()" function as an argument to the "list()" function

numbers = list(range(1, 100 + 1))
print(numbers)

# Let us also use the "list()" function and pass a string
chars = list("Hello World")
print(chars)

# The output will be each character in our original string will be an item in the resulting list
# These are a few different ways to create a list in Python

# Now that we have a list, we can get the number of items in the list using the "len()" function
print(len(chars))


print(len(numbers))

print(len(combine))
