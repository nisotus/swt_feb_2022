# In this section we will look at how to loop over lists
# Below we have a list of items

# letters = ["a", "b", "c", "d"]

# we can use a FOR LOOP to loop over the list

# for letter in letters:
#     print(letter)
    
# What if we want to get the index or position of each item/element in the list
# We have a built-in function called "enumerate()"
# The enumerate() function takes an iterable as argument

# letters = ["a", "b", "c", "d"]
# for letter in enumerate(letters):
#     print(letter)
    
# The enumerate() function will return an enumerate object which is iterable
# In each iteration, the enumerate() object will give us a TUPLE of two items
# The first item in the TUPLE is the index and the second item is the item at that index

# letters = ["a", "b", "c", "d"]
# for letter in enumerate(letters):
#     print(letter[0])  # here we are accessing the TUPLE index 0
    
# letters = ["a", "b", "c", "d"]
# for letter in enumerate(letters):
#     print(letter[1])  # here we are accessing the TUPLE index 1
    
# letters = ["a", "b", "c", "d"]
# for letter in enumerate(letters):
#     # here we are accessing the TUPLE indexes 0 and 1
#     print(letter[0], letter[1])
    
# This code is a little ugly - print(letter[0], letter[1])
# There is a better way to write it
# letters = ["a", "b", "c", "d"]
# items = [0, "a"]  # This is a list
# index, letter = items  # Unpacking the items list
# for letter in enumerate(letters):
#     print(letter[0], letter[1])

# The UNPACKING will also work for a TUPLE
    
# letters = ["a", "b", "c", "d"]
# items = (0, "a")  # This is a list
# index, letter = items  # Unpacking the items list
# for letter in enumerate(letters):
#     print(letter[0], letter[1])
    
# So to make the code cleaner, we can use the UNPACKING in the FOR statement

# letters = ["a", "b", "c", "d"]
# items = (0, "a")  # This is a list
# index, letter = items  # Unpacking the items list
# for index, letter in enumerate(letters):
#     print(index, letter)
    
# So the final program will look like below:

letters = ["a", "b", "c", "d"]
for index, letter in enumerate(letters):
    print(index, letter)
    

# To recap
# We can use FOR LOOPS to iterate over LISTS
# If you also need the INDEX, you should call the enumerate() function
# The "enumerate()" function will return an enumerate object which is iterable
# In each iteration, the "enumerate()" function  will return a TUPLE
# And you can UNPACK the TUPLE right in the FOR statement of the FOR LOOP