# In Python we have another very useful data structure called a "SET"
# A SET is basically a collection with no duplicates

# # Let's say we have a list of numbers with a bunch of duplicate items

# numbers = [1, 1, 2, 2, 3, 4, 5, 5]

# # We can remove the duplicates in the list above by converting the LIST to a SET
# # To do this we use the set() function

numbers = [1, 1, 2, 2, 3, 4, 5, 5]
unique = set(numbers)
print(unique)

# # Also note that we use CURLY BRACES {} to define SETS

# # So let us define a SET called "second"
# second = {1, 4}

# # Similar to lists, we can add new items or remove existing ones from a set

# # We can add a new item using the add() method

# second.add(5)
# print(second)

# # We can remove an new item using the remove() method

# second.remove(5)
# print(second)

# # We can use the len() function to get the number of items in a SET

# print(len(second))

# # This is the basics of SET
# # Let us now look at where SETS shine

# # *** Where does SETS shine? *** 
# # SETS shine in the powerful mathematical operations that are supported by them
# # Let's have a look.

# # Below we have two SETS - "first" and "second"
# number = [1, 4, 1, 5, 2, 2, 3]
# first = set(number)
# second = {1, 5, 5, 6}

# # We can get a union of two sets using a vertical bar "|" operator
# #This will include all the items that are either in the first or the second SET

# print(first | second)

# # We can get the intersection of two SETS using the "&" operator
# # This will return a new set that includes all the items
# # That are in both "first" and "second" SETS

# print(first & second)

# # We can get the difference between two SETS using the minus "-" operator
# # This will return the items we have in the "first" SET
# # but that we don't have in the "second" SET

# print(first - second)

# # We can get the symmetric difference between two SETS using the caret "^" operator
# # This will return the items that are either in the "first" SET or "second" SET 
# # but not both

# print(first ^ second)

# # *** Differences between SETS and LISTS
# # One thing to know about SETS is that unlike LISTS, SETS are unordered collections
# # Which means that items we have in a SET are not in sequence
# # So we cannot access them using an index

# # Below will not work'
# # You will get an error - "TypeError: 'set' object is not subscriptable"

# # print(first[0])

# # So if you need to access items by index, you need to use a LIST, a TUPLE

# # We can also check to see the existence of an item in a SET

# if 5 in second:
#     print("exists")

# # *** To recap
# # SET is an unordered collection of uniques items
# # We cannot have duplicates, and its objects are unordered
# # They are not in sequence, so we cannot access them using an index.