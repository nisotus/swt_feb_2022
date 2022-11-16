# If we look at the piece of code below
# What will be the result when we run it?

# values = []
# for x in range(5):
#     values.append(x * 2)
#     print(values)
    
# What about the code below
# What will be the result when we run it?

# values = []
# for x in range(5):
#     values.append(x * 2)

# print(values)

# Whenever we have the pattern below:
# values = []
# for x in range(5):
#     values.append(x * 2)

# We can either use the map() function or the LIST COMPREHENSION

# This is the SYNTAX for LIST COMPREHENSION - "[expression for item in items]"

# *** Explanation of the LIST COMPREHENSION - "[expression for item in items]"
# We iterate over an iterable - "items" or "x"
# In each iteration we get - "item" or "x" = iteration variable
# And then do something = "expression" with each - "item"

# *** Using the example we have 
# values = []
# for x in range(5):
#     values.append(x * 2)
# print(values)
    
# Iterable = range(5)
# Iteration variable = x
# Expresssion = x * 2
# The we store the result in "values"

# Use the above explanation to write a LIST COMPREHENSION statement

# values = [x * 2 for x in range(5)]
# print(values)

# names = ["jay", "tay", "bay"]

# name_mul = []
# for name in names:
#     name_mul.append(name * 2)

# print(name_mul)

# *** COMPREHENSIONS in SETS and DICTIONARIES
# COMPREHENSIONS are not limited to LISTS
# We can also use them in SETS and DICTIONARIES

# If we replace the angle brackets "[]" with curly brackets "{}" we get a set:

# values = {x * 2 for x in range(5)}
# print(values)

# *** Difference between SETS, LISTS, and DICTIONARIES
# Now, what is the syntactical difference between a SET and a DICTIONARY
# In SETS, LISTS we have only VALUES
# In DICTIONARIES we have KEY/VALUE pairs that are separated using a colon ":"

# So we can easily use COMPREHENSION EXPRESSIONS to create DICTIONARY objects
# So in our example, all we need to do is to change the expression such that we have a KEY/VALUE pair
# In our example, we use "x" as the KEY.

# values = {x: x * 2 for x in range(5)}
# print(values)

#****************

dict = {"a": 1, "b": 2, "c": 3, "d": 4}

values = {}
for x, y in dict.items():
    print(x, y*2)
    
#values = {x: y * 2 for x, y in dict.items()}
#print(values)

# So instead of defining and empty dictionary "values = {}"
# then looping over an iterable "range(5)"
# and then in each iteration, adding something to the dictionary like -
# "values.append(x * 2)" OR "values[x] = x * 2"

# Whenever you have this type of pattern in your code
# We can use DICTIONARY COMPREHENSION

# *** To recap
# We can use COMPREHENSIONS with
# LISTS
# SETS
# DICTIONARIES

# Tuple example
#values = (x * 2 for x in range(5))
#print(values)

# We get the error - "<generator object <genexpr> at memory address>"

# Now this is the topic for the next session = GENERATOR EXPRESSIONS