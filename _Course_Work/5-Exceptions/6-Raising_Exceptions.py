# So far we have lerant how to handle exceptions,
# but you can also "raise" or "throw" exceptions in your own code

# Let's see an example:

# def calculate_xfactor(age):
#     return 10 / age

# In the example above, "age" cannot be "0" or less

# So we can add an IF STATEMENT and "raise" an exception
# Using the "raise" statement and specify the type of exception

# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be 0 or less")
#     return 10 / age

# calculate_xfactor(0)

# **** Built-in exceptions in Python
# In Python we have various kinds of built-in exceptions
# Go to - https://docs.python.org/3/library/exceptions.html

# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be 0 or less")
#     return 10 / age

# calculate_xfactor(-1)

# The program will crash with a ValueError exception like below:
# ValueError: Age cannot be 0 or less

# The crash happened because we did not handle the exception properly
# when we called the "calculate_xfactor()" function

# To fix this issue, we add a "try" block with an except clause of type
# "ValueError()" around the "calculate_xfactor()" function call


# Solution 1

# def calculate_xfactor(age):
#     try:
#         if age <= 0:
#             raise ValueError("Age cannot be 0 or less")
#         return 10 / age
#     except ValueError:
#         print("Agen cannot be 0 or less")

# calculate_xfactor(-1)

# Solution 2
# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be 0 or less.")
#     return 10 / age


# try:
#     calculate_xfactor(-1)
# except ValueError:
#     print("Age cannot be 0 or less.")
    
# ***We can also use the approach below
# Where we save the "ValueError()" as a variable "error"
# and then print out the content of the "error" variable

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
    
# *** Raising exceptions is not always advisable
# Raising exceptions is not always advisable
# We explain it here because you will see it in other people's code

# *** Raising exceptions is costly
# So intead of raising an exception in the function creation and then handling it in the function call,
# we can take a different approach that would result in better perfmance

# This is what we will look at next.