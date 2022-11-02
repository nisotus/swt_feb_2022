# C R U D S

# C = Create
# R = Read
# U = Update / Manipulate
# D = Delete
# S = Secure


# In this section we will look at how to add items to a list
# Or remove existing items

# *** Reminder - Everything in Python is an object
# *** So we can use the dot(.) notation to access
# *** individual functions or more accurately methods in that object
# *** So when a function is part of an object, we refer to that function as a method


# ***ADD***
# For adding items, you have two options depending on where you want to add the item
# To add an item at the end of the list - use the "append()" method
# letters = ["a", "b", "c", "d"]
# letters.append("e")
# print(letters)

# To add an item at a specific position in the list, you should use the "insert()" method
# letters = ["a", "b", "c", "d"]
# letters.insert(0,"z")
# print(letters)

# ***REMOVE***
# For removing items, we have different options
# To remove an item at the end of the list - use the "pop()" method

# letters = ["a", "b", "c", "d"]
# letters.pop()
# print(letters)

# You can also pass an index to "pop()" method to remove the item at that index
# letters = ["a", "b", "c", "d"]
# letters.pop(2)
# print(letters)


# How do you remove an item when you don't know it's index?
# In that case you can use the "remove()" method
# This will remove the first occurence of the item
# letters = ["a", "b", "c", "b", "d" , "b"]
# letters.remove("b")
# print(letters)

# If you want to remove all items that are these same in a list (for example all "b"s in a list)
# You will have to loop over the list and remove each "b" individually

# We have another way to remove an item from the list
# This is by using the "del" statement
# With the "del" statement, we can delete an item by the index

# Using the "del" keyword
# letters = ["a", "b", "c", "d"]
# del letters[3]
# print(letters)

# We can also delete a range of items using the "del" statement
# letters = ["a", "b", "c", "d"]
# del letters[0:2+1]
# print(letters)

# letters = ["a", "b", "c", "b", "d" , "b"]

# for i in letters:
#     if i == "b":
#         letters.remove("b")
# print(letters)

#********************************

# The one we were unable to solve.....
# letters = ["a", "b", "c", "b", "d" , "b"]

# for i in letters:
#     if i is not numeric:
#         letters.remove(i)
# print(letters)

#*************************
# letters = ["a", "b", "c", "b", "d" , "b"]

# for i in letters:
#     letters.clear()

# print(letters)

#*************************
# letters = ["a", "b", "c", "b", "d" , "b"]

# for i in letters:
#     letters.pop(-1)

# print(letters)

# The difference bewteen the "del" statement and the "pop()" method
# The "pop()" method will remove only one item by index
# With the "del" statement we can remove a range of items


# Finally is you want to remove all items in the list
# You should use the "clear()" method
# letters = ["a", "b", "c", "d"]
# letters.clear()
# print(letters)
