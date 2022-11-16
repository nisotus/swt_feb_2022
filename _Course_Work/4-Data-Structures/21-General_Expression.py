# Tuple example
# values = (x * 2 for x in range(5))
# print(values)


# Below we are creating a LIST using a LIST COMPREHENSION EXPRESSION
# Then we iterate over all the numbers in the LIST and PRINT them
# values = [x * 2 for x in range(10)]
# print(values)

# When we run this program we get the even numbers from 0 to 18

# When working with a really large dataset, for example an infinite stream of data
# You should not store all those values in the memory

# For example, let's say instead of range(10), you have range(1000000000)

# In stuations like this it is better to use a GENERATOR OBJECT

# So unlike LISTS, GENERATORS don't store all the VALUES in memory
# They generate a new value in each iteration

# **** Let's see how it works
# Let's replace the square brackets "[]" with "()"
# values = (x * 2 for x in range(10))
# print(values)

# If we write the code like below, the GENERATOR OBJECT will no longer appear in our result
# values = (x * 2 for x in range(10))
# for x in values:
#     print(x)

# However, if we write the code like below, the GENERATOR object will appear in our result
# values = (x * 2 for x in range(10))
# print(values) # <generator object <genexpr> at 0x00000204BDA09A10>
# for x in values:
#     print(x)
    
# GENERATOR OBJECTS are ITERABLE, we can iterate over them
# At each iteration they spit out a new value

# *** What is interesting is:
# The size of generator objects

#*** Getting the size of objects
# To get the size of any object, we need to import "getsizeof" function from "sys" module
# Call getsizeof() function and pass the generator object "values" and then print the result
# We can also add a label "gen" in the print() function

# from sys import getsizeof
# values = (x * 2 for x in range(10))
# print("generator_object_size:", getsizeof(values))

# What if we change the to range(100000)

# from sys import getsizeof
# values = (x * 2 for x in range(100000))
# print("generator_object_size:", getsizeof(values))

# Notice that the size of the generator object remains consistent = 104 bytes

# In contrast, if we use a LIST COMPREHENSION
# Let us compare the size of the generator object

# from sys import getsizeof
# values = (x * 2 for x in range(100000))
# print("gen", getsizeof(values))

# values = [x * 2 for x in range(100000)]
# print("list", getsizeof(values))

# You will see that out LIST is taking over eighty thousand (80,000) bytes of memory
# Compared to our GENERATOR OBJECT that takes only 104 bytes of memory

# So in situations where you are dealing with a really large DATA SET
# OR potentially an INFINITE STREAM of DATA, use a GENERATOR EXPRESSION
# To create a GENERATOR OBJECT

# *** Downside!!!
# When we use parenthesis "()" around a COMPREHENSION EXPRESSION
# Just be aware that because  GENERATOR OBJECTS don't store all the items in memory
# You won't be able to get all the total number of items you are working with


# For example, let's just keep the GENERATOR OBJECT
# and then print the length of "values" using the len() function

# *** Code that produce error!
values = (x * 2 for x in range(100000))
print(len(values))

# When we run this code, we will get an error -
# "TypeError: object of type 'generator' has no len()"

# So we won't know ahead of time, how many objects or how many items the GENERATOR is going to produce.