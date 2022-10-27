# ********* CRUD

# Create Data
# Read Data
# Update Data
# Delete data

# Accessing List items

# To access items in a list, we can use square brackets "[]" and the index value of the item to access individual items in a list
# letters = ["a", "b", "c", "d"]
# print(letters[3])

# What will be the output of below
# letters = ["a", "b", "c", "d"]
# print(letters[-4])

# Using square brackets "[]" we can also modify the items in the list
# letters = ["a", "b", "c", "d"]
# letters[0] = "A"
# print(letters)

# We can use the square brackets "[]" and two index values to slice the items in a list
# This will return a new list with the first 3 items in our original list
letters = ["a", "b", "c", "d"]
# letters[2] = "z"
# print(letters)

# print(letters[0:3])

# If we print our original list, what will be the result?
# You will see that it has not changed
# print(letters)

# ************
# What will be the result of below?
# print(letters[:3])

# What will be the result of below?
# print(letters[0:])

# What will be the result of below?
# print(letters[:])

# When slicing a string, you can also pass a STEP using an additional colon within the square brackets [::]
# This is useful in a situation where you want to return every second or third element in the original list

# print(letters[::1])  # returns every element in the list

# print(letters[::2])  # returns every second element in the list

# print(letters[::3])  # returns every third element in the list

# print(letters[::4])  # returns every fourth element in the list

# num = list(range(1, 100 + 1))
# print(num[::7])

# let's use a better example
numbers = list(range(21))
# print(numbers)
# print(numbers[::2])
# print(numbers[::4])
# print(numbers[::5])
# print(numbers[5::5])

# What about below, what will be the result?
print(numbers[::-1])

print(numbers[::-2])

print(numbers[::-5])

print(numbers)

print(numbers[3::-1])
