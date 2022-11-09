# list = ["a", 1, 2, 3, "Joe", "Nigeria", True, False, False]
# list.append("Jessica")
# list.pop(4)
# print(list)

# tuple1 = ("a", 1, 2, 3, "Joe", "Nigeria", True, False, False)
# list.append("Jessica")
# list.pop(4)
# print(list)

# In this section we are going to take a closer look at TUPLES
# A TUPLE is basically a read only list.
# We can use it to contain a sequence of objects
# But we cannot modify the sequence, we cannot remove an existing object
# We cannot add a new object and we cannot modify an existing object

# To define a TUPLE we use parenthesis "()" instead of square brackets "[]"

# In Python, whenw orking with TUPLES, we can actually exclude the parenthesis
point1 = (1, 2, 3)
point2 = 1, 2, 3

print(type(point1))
print(type(point2))

# What if I have only one item in my TUPLE, and I want to define it without parenthesis
point3 = 4,
point4 = 4 # This is an integer

print(type(point3))
print(type(point4))

# How do we define and empty TUPLE
empty_tuple = ()
print(type(empty_tuple))

# Similar to lists, we can concatenate two Tuples
point6 = (7, 8) + (9, 10)
print(point6)

# We can also use the multiplication operator to repeat a Tuple
point7 = (5, 8) * 3
print(point7)

# We can convert a LIST to a TUPLE using the "tuple()" function
# The "tuple()" function takes an iterable as argument

my_list = ["a", 1, 2, 3, "Joe", "Nigeria", True, False, False]
my_tuple = tuple(my_list)
print(my_tuple)

# We can convert a TUPLE to a LIST using the "list()" function
# The "list()" function takes an iterable as argument
my_tuple = ("a", 1, 2, 3, "Joe", "Nigeria", True, False, False)
my_list = list(my_tuple)
print(my_list)

# We can pass any iterable object to the "tuple()" function
# and the "tuple()" function will return a Tuple
my_word = "How are you doing?"
my_tuple_word = tuple(my_word)
print(my_tuple_word)

# Similar to LIST we can access individual items using the index
point = (1, 2, 3)
print(point[0])

# We can get a range of items like index 0 to index 2 [0:2]
# This returns another TUPLE with only the objects sliced

point = (1, 2, 3)
print(point[0:2])

# We can UNPACK TUPLES

point = (1, 2, 3)
x, y, z = point
print(x)
print(z)

# Similar to List, we can use the "in" operator
# To check for the existence of an item in a Tuple

point = (1, 2, 3)
if 10 in point:
    print("exists")
else:
    print("Does not exist")
 
# using the FOR LOOP on TUPLES    
for p in point:
    print(p)
    
# We cannot change the items in a TUPLE.
# TUPLE is immutable, so the code below will not work
# You will get the error: "TypeError: 'tuple' object does not support item assignment"

point[0] = 10

# For this reason UNLIKE LISTS, we don't have METHODS
# To add/remove items or objects to/from a TUPLE

# *** QUESTION
# So where in the real world do we use TUPLES?
# Here is a basic rule of thumb
# Use TUPLE when you want to prevent accidentally adding/removing an object