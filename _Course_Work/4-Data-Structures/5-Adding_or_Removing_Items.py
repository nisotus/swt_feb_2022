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
letters = ["a", "b", "c", "d"]
letters.pop()
letters.pop()
letters.pop()
letters.pop()
print(letters)