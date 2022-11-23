# When writing your own functions, it is preferred not to raise exceptions
# because these exceptions come come with a cost

# From the "timeit" module, import the "timeit" function
# With the "timeit" function, we can calculate the execution time of some Python code

from timeit import timeit

# To calculate the execution time of a piece of code
# We define a variable and set it to a string
# The string should include the Python code

# code1 = """
# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be 0 or less.")
#     return 10 / age


# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     print(error)
# """

# The function below will calculate the execution time and return it
# timeit(code1, number=10000)
# So we can simple print it to the terminal

# print("firstcode=", timeit(code1, number=10000))

# Let's clean this up a litte by replacing the code "print(error)" with the "pass" statement

# code1 = """
# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be 0 or less.")
#     return 10 / age


# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     pass
# """

# print("firstcode=", timeit(code1, number=10000))


# Save the changes and run the program again and yu will get the total execution time

# *** A different approach
# Now let us try a different approach
# In the "calculate_xfactor()" function, instead of raising an exception, if age is zero or less
# We can return  value like "None" - None is an object that reresents the absence of a value

# In this new implementation, we don't need a "try" and "except" block. So we can delete them

# We simply store the result of the function "calculate_xfactor()" in a variable
# we can call the variable "xfactor"

# So instead of handling an exception, we can compare the content of variable "xfactor" with "None"
# If "xfator" == None, then we just "pass" = Do Nothing

#**********************************

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass

"""
print("second code=", timeit(code2, number=10000))

# As a general rule of thumb, when you want to raise exceptions in your program
# *** Think Twice
# See if you can handle the situation with a simple IF STATEMENT
# You code will end up being a bit cleaner whether there is performance difference or not

# So raise exceptions if you really have to