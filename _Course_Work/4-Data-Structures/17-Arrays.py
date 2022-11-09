# So we have learnt a lot about LISTS in Python. These lists are very useful
# But if we are dealing with a large sequence of numbers
# We have a more efficient data type in Python called "ARRAY"

# These ARRAYS take less memory and perform a little bit faster
# Note that you will see the difference only if you are dealing with
# A large list of numbers, lets say 10,000 (ten thousand) or more

# For 90% of the cases, you would use list
# But if you run your program and you see some performance problems
# Then you can see if you can solve the problem by replacing a LIST with an ARRAY

# But don't try to optimize if you don't have any performance problems
# Don't try to solve a problem that does not exist.

# So let's look at how to use ARRAYS in Python

# *** How to use an ARRAY in Python ***
# To use an array, we need to import it from the "array" module
# So we have a module called "array" and in the module
# we have a class called "array"

from array import array

# Now we can call array() class

# *** The first parameter is "typecode"
# "typecode" is a string that determines the type of objects in the array

# In google you can search for "Python 3 typecode" - https://docs.python.org/3/library/array.html
# You will see all the typecodes in Python
# So the typecode is a string of one character that determines the type of object in your LIST
# For example if you are dealing with signed intergers you should use a lower case "i"


# *** Second Argument
# As the second argument to the "array" function, we pass a LIST

my_list = [1, 2, 3]
array("i", my_list)

# Now we get an array, we can call it whatever we like. Lets call it numbers

numbers = array("i",[1, 2, 3])

# In this array object, similar to LISTS, we have methods
# For adding new objects OR removing existing ones

# We can append a number to the end of the LIST using the append() method

numbers.append(4)
print(numbers)

# We can insert a number at any index in the LIST using the insert() method

numbers.insert(4, 5)
print(numbers)

# We can remove a number from the LIST using the remove() method

numbers.remove(2)
print(numbers)

# We can pop a number from the end of the LIST using the pop() method

numbers.pop()
print(numbers)

# We can also access items by their index

print(numbers[0])

# *** Difference from LIST
# Unlike LISTS, the objects in the array are typed
# So in our example, every object should be an integer

# If you try to put a floating point number OR any other kind of objects
# You will get an error

# For example, below will not work

# numbers[0] = 1.0

# You will get the error - "TypeError: integer argument expected, got float"

# So every object in the array must be of the same type
# and this is determined at the time of creating the array using the "typecode"

# *** To recap
# Use ARRAYS when dealing with a large sequence of numbers and you encounter performance problems
# For other cases, use LISTS and TUPLES by default.