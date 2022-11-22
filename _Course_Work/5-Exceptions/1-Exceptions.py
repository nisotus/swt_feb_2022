# When writing programs, many things can go wrong
# Our programs may envounter an error and terminate

# These errors happen due to:
# 1. Programmers mistake
# 2. Bad data that that the user enters
# 3. Resources not available

# For exampl, you might need to open a file
# But if the file does not exist, the program will crash

# It's your job as a programmer and/or tester to prevent your application from crashing
# In this kind of situations, instead you want to display a proper error message to the user
# like, "hey, this file does not exist"

# So let's take a look at some examples

# numbers = [1, 2]
# print(numbers[2])

# If you run this program you will get an error - "IndexError: list index out of range"

# In programming we refer to this kind of error as an EXCEPTION
# An exception is a kind of error that terminates the execution of a program

# The example of an exception that was thrown because of the programmer's mistake is below:

age = int(input("Age: "))

# If you run this program and enter "a" = non-integer value for "age"
# you will get an error - "ValueError: invalid literal for int() with base 10: 'a'"

# So, how do we prevent this?