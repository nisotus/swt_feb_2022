# In this section we will how to chain comparison operators
# This is a very powerful technique for writing clean code

# Here is an example:
# Let's say we want to implement a rule that age should be between 18 and 65

age = 22
if age >= 18 and age < 65:
    print("Eligible")

# A question for you is how do we write the expression in mathematics?
# We write it like this: 18 <= age < 65

# We can write the exact same equivalent in Python

age = 22
# if age >= 18 and age < 65:
if 18 <= age < 65:  # This is cleaner and easier to read.
    print("Eligible")


# This is what we call Chaining Comparison Operators
