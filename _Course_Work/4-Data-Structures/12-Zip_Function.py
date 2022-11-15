# Below we have two lists

list1 = [1, 2, 3]
list2 = [10, 20, 30]

# Let's say we want to combine these two lists into a single list of TUPLES like below:

# *** The TUPLE
# We have a list, where each item is a Tuple
# First Tuple - we are going to have the first element of each list - list1 and list2
# Second Tuple - we are going to have the second element of each list - list1 and list2
# Third Tuple - we are going to have the third element of each list - list1 and list2

[(1, 10), (2, 20), (3, 30)]

# How can we combine list1 and list2 into a single list like - [(1, 10), (2, 20), (3, 30)]

# *** Note
# Note that we cannot use the MAP or LIST COMPREHENSION to achive this,
# because map() and List Comprehension only works with one List.
# But here we are combining multiple lists

# *** How to do this?
# To achive this we use the built-in "zip()" function
# The zip() function takes multiple iterables
# and it will combine them just like this - [(1, 10), (2, 20), (3, 30)]

list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip(list1, list2)))
print(list(zip("abc",list1, list2)))
