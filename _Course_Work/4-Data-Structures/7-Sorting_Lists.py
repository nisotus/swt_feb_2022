# numbers = [3, 51, 2, 8, 6]
# We can sort the list by calling the "sort()" method on the list
# Note that the sort() method sorted the items in ascending order

# *** ASCENDING ORDER
# numbers = [3, 51, 2, 8, 6]
# numbers.sort()
# print(numbers)

# *** DESCENDING ORDER
# What if you want to sort the list in descending order?
# The sort() method takes two parameters "key" and "reverse"
# We will look at the parameter "key" later

# You can reverse the order by setting "reverse=True"

# numbers = [3, 51, 2, 8, 6]
# numbers.sort(reverse=True)
# print(numbers)

#********************************
# The sorted() function
# The sorted() function will return a new list that is sorted
# Unlike the sort() method, the sorted() function will not modify the original list
# The sorted() function will return a new sorted list

# numbers = [3, 51, 2, 8, 6]
# print(sorted(numbers))
# print(numbers)

# Also similar to the sort() method
# You can change the sort order by setting the "reverse" argument to "True"
# numbers = [3, 51, 2, 8, 6]
# print(sorted(numbers, reverse=True))
# print(numbers)

#******************************

# *** SORTING COMPLEX OBJECTS
# Sorting numbers and strings is pretty easy, but what if we are dealing with a list of complex objects
# For example, what if we have a list of TUPLES. Let's imagine we are building an application
# for processing orders and we have a list of order items where every item in the list is a TUPLE
# Like below:
# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12)
# ]

# What happens if we try to sort this list?
# let's take a look

# items.sort()
# print(items)

# Nothing is changed, because Python does not know how to sort the list

# ***********************************
# In situations like this, we need to define a function that Python will use for sorting the list
# See the program below:

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
#     ("Product4", 1),
#     ("Product6", 102),
#     ("Product5", 3), 
#     ("Product10", 3)   
# ]
# # print(items[0])

# def sort_item(item):
#     return item[1]

# items.sort(key=sort_item)
# print(items)

# Now, let's sort by product.
# To do this, we just need to change the "return item[1]" to "return item[0]"


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
    ("Product4", 1),
    ("Product6", 102),
    ("Product5", 3), 
    ("Product10", 3)   
]
# print(items[0])

def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)



# *** BETTER WAY
# The way we have implemented the sort function - "sort_item(item)" - is a little bit ugly
# There is a better way and that is what we will look at next - LAMBDA FUNCTIONS






#********************* Muyiwa's Solution ************
# empty = []

# for num in numbers:
#     if num not in empty:
#         empty.append(num)
#         empty.sort()

# print(empty)

