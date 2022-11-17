# One operator that comes handy when working with DATA STRUCTURES is the UNPACKING OPERATOR - "*"

# Let's say we have a list of numbers:

# numbers = [1, 2, 3]

# If we print "numbers"
# print(numbers)
# We get the LIST of numbers but in a LIST

# If we want to print individual numbers, we can use a FOR LOOP
# for n in numbers:
#     print(n)
    
# What if we don't want to use a FOR LOOP
# and we still want to be able to print individual numbers

# To achieve this we can use the UNPACKING OPERATOR - "*"
# All we have to do is prefix the list variable with the UNPACKING OPERATOR - "*"

# numbers = [1, 2, 3]
# print(numbers)
# print(*numbers)

# In JavaScript, we have an operator called "SPREAD OPERATOR" with three dots "..."
# The SPREAD OPERATOR in JavaScript does exactly the same thing as the UNPACKING OPERATOR in Python

# Another useful application of this is when creating LISTS
# Let's say we want to have the LIST of numbers from 0 - 5 using a range() function

range(5)

# We know that the range() function returns a range object
# So we need to convert it to a LIST.
# Store the result in a variable and print the list

# values = list(range(5))
# print(values)

# In this case, instead of calling the list() function
# We can use the UNPACKING OPERATOR and store the UNPACKED values in a LIST

# values = [*range(5)]
# print(values)

# The good thing about the UNPACKING OPERATOR is that we can UNPACK any ITERABLE

# This means that we can also UNPACK a STRING

# word = [*"Hello"]
# print(word)

# Using the UNPACKING OPERATOR we can combine multiple LISTS
# first = [1, 2, 3, 4]
# second = [5]

# values = [*first, *second]
# print(values)


# We can also put something in the middle OR UNPACk a string at the end
# values = [*first, "a" , *second, *"Hello"]
# print(values)

# The UNPACKING OPERATOR is really powerful.

# We can also UNPACK a DICTIONARY
# first = {"x": 1}
# second = {"x": 10, "y": 2}
# combined = {**first, **second}
# print(combined)

# Note that the value of KEY "x" is 10
# This is because if you have multiple VALUES with same KEY, the last VALUE will be used

# We can also add another KEY/VALUE pair in the middle or at the end when working with DICTIONARIES
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, "r": 13, **second, "z": 14}
print(combined)

# *** To Recap:
# We can use the UNPACKING OPERATOR to take out individual values in any ITERABLE