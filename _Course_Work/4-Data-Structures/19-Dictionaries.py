# In Python we have a very powerful data structure called "DICTIONARY"
# A DICTIONARY is basically a collection of KEY/VALUE pairs
# We use it to map a KEY to a VALUE

# Real world examples of this are Phone Book and Language Dictionary

# In a Phone Book, we map a person's name to their contact details
# KEY = name and VALUE = contact details

# In a Language Dictionary, we map a words to their meaning/definition
# KEY = word and VALUE = definition

# *** How to work with DICTIONARIES in Python
# We use CURLY BRACES "{}" when creating DICTIONARIES

# [] for lists

# () for tuples

# {} for sets

# {} for dictionaries

# We can have an empty dictionary
# point = {}

# We can have a dictionary that contains key/value pairs
# point = {"x" : 1, "y" : 2, "z" : 3}

# In the example above, we are using a string for the KEY and an integer for the VALUE

# *** Note
# In Python, we can only use IMMUTABLE/UNCHANGING types for the KEY
# So quite often we use STRINGS and NUMBERS

# But the VALUE can be of any TYPE, there are no limitations

# *** Using the dict() function to define a DICTIONARY
# Just like we have:
# list()
# tuple()
# set()

# point = dict(x=1, y=2, z=3)
# print(point)

# We can get the VALUE associated with a KEY using an index
# *** Note that the index should be the name of a KEY

# Because DICTIONARIES are collections of KEY/VALUE pairs
# We cannot access an item using a numeric index like - point[0], like we do with LIST

# print(point["x"])

# We can change the VALUE of KEY "x"

# point["x"] = 10
# print(point)

# We can add a new key "p"
# point["p"] = 20
# print(point)


# When reading a VALUE, if we use an invalid KEY
# print(point["a"])
# We get an error - "KeyError: 'a'"


# *** Workarounds for the error
# There are two workarounds that we can use

# *** Solution 1
# Check for the exitence of the key
# if "a" in point:
#     print(point["a"])

# *** Solution 2
# Using the "get()" method
# If the KEY does not exist, by default it returns "None"
# print(point.get("a"))

# We can also pass a default value as a second argument to the "get()" function
# Meaning if you don't have an item with the KEY "a", return "0" by default
# print(point.get("a", 0))

# *** Other methods you can use on DICTIONARIES

# To delete an item, we use the del() method

# del point["x"]
# print(point)


# How do we LOOP over DICTIONARIES?

# For example to LOOP over a LIST, we can do below: 
# my_list = [1, 2, 3, 4]

# total = 0

# # sum = sum(my_list)
# for i in my_list:
#     total = total + i

# print(total)

# Let's try doing this for a DICTIONARY

# my_dict = dict(x=1, y=2, z=3)
# print(my_dict)

# for i in my_dict:
#     print(i)
    
# Notice that only the KEYS were printed

# Now to print the VALUES, we need to access the VALUES using the KEY
# my_dict = dict(x=1, y=2, z=3)

# for i in my_dict:
#     print(i, my_dict[i])
    
# Let us re-write the code for easier reading
# my_dict = dict(x=1, y=2, z=3)

my_dict = dict(x=1, y=2, z=3)
for key in my_dict:
    print(key, my_dict[key])
    
# ********************************************


# There is another way to iterate over a dictionary
# We can use teh items() method on the dictionary

# my_dict = dict(x=1, y=2, z=3)
# items = my_dict.items()
# print(items)

# This will give us - dict_items([('x', 1), ('y', 2), ('z', 3)])

# *** Using the items() method
# my_dict = dict(x=1, y=2, z=3)
# for x in my_dict.items():
#     print(x)


# When we use point.items(), in each iteration we will get a TUPLE
# In the TUPLE, we have the KEY and the VALUE
# So we can UNPACK the TUPLE in the FOR SATEMENT like below

my_dict = dict(x=1, y=2, z=3)
for key, value in my_dict.items():
    print(key, value)