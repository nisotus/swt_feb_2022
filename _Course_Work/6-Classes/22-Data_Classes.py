# We already know that we use classes to bundle data and finctionality into one unit
# As you work on larger programs, you may come across classes that don't have any behaviour
# Meaning they don't have methods, they only have data

# Below is an example:

# You have a "Point" class that has two attributes "x" and "y"
# It does not have any methods

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# Now with this we can create two "Point" objects

# p1 = Point(1, 2)
# p2 = Point(1, 2)

# When we compare the two objects "p1" and "p2" and print the result, we get "Flase"
# print(p1 == p2)

# This is because these two objects "p1" and "p2" are stored in different locations in memory
# So by default Python compares objects based on where they are stored in memory
# If two variables are referencing the same object in memory, they are considered equal

# In this example, our "Point" objects - "p1" and "p2" are in two different locations
# even though they have the same attributes

# To prove this, we are goin to call the built in "id" function
# The "id" function returns the address of the memory location where an object is stored

# print(id(p1))
# print(id(p2))

# print(p1)
# print(p2)

# As you can see these objects are in two different locations in memory

# *****************************
# To solve the issue with comparing "Point" objects
# we need to implement a magic method called "__eq__"
# Method "__eq__" takes "self" and "other" as parameters
# Then we can return "self.x == other.x and self.y == other.y"

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
    
# p1 = Point(1, 2)
# p2 = Point(1, 2)
# print(p1 == p2)

# Now when we compare the objects "p1" and "p2" we get the result "True"

# *********************
# However, writing all the code below for data classes is a little bit tedious

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y


# **********************
# **********************
# If you are dealing with classes that have no behaviour, no methods, they only have data
# You can use a "NAMED TUPLE" instead. let's see how that works:

# From the "collections" module, import the "namedtuple" function

from collections import namedtuple


# We call the function "namedtuple"

# As the first argument we specify the name for the new type we want to create
# So we call that "Point" - Note that we passing "Point" as a string

# As a second argument, we pass an array of field/attribute names ["x", "y"]
# This is because we want our point objects to have two attributes "x" and "y"
# So we have *namedtuple("Point", ["x", "y"])*
# This returns a NAMED TUPLE that we can store in "Point" - Note that we are using Pascal naming convention
# because "Point" here represents a TYPE, like a CLASS, so we can call it to create a new "Point" object

# ******************************
# However, instead of passing the arbitrary values "(1, 2)"
# We should pass KEYWORD ARGUMENTS "x=1", "y=2"

Point = namedtuple("Point", ["x", "y"])

p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)

# *** The first benefit ***
# The first improvement here is that our code is more clear and less ambiguous
# We don't have to wonder what these values "x"  and "y" are

# *** The second benefit ***
# The second benefit is that we don't have to excplicitly implement a magic method to compare two objects
# So if we have two "Point" objects with the exact same attributes
# you can easily compare them and we get the result that we expect

# ***********************
# So if you are working with classes that have only data and no methods
# You might want to use a "namedtuple" instead
# You will write less code and these namedtuples are better than normal tuples
# because we have attributes in the "Point" object just like the attributes we have in our classes

# ***********************
# So if we print p1.x = print(p1.x) we see "1" as the result

print(p1.x)
print(p1.y)

# **********************
# Just be aware that these namedtuples are IMMUTABLE
# Which means once we create them we cannot modify them

# So if we set p1.x to a new value , like "p1.x = 10" and run the program, we get an attribute error

Point = namedtuple("Point", ["x", "y"])

p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
# p1.x = 10  # AttributeError: can't set attribute
print(p1 == p2)

# **********************
# So if you really need to modify one of these values "x" and "y"
# You need to create a new "Point" object
# So we set "p1" to a new "Point" like "p1 = Point(x=10, y=20)"

Point = namedtuple("Point", ["x", "y"])

p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
p1 = Point(x=10, y=20)
print(p1 == p2)

# *** So this is all about named tuples