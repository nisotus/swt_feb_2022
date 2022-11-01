# There are times that you want to find the index of a given object in a list
# Let's say we want to find the index of the letter "a" in the "letters" list

# We can do this by calling the "index()" method on the list

# letters = ["a", "b", "c", "d"]
# print(letters.index("z"))

# letters = ["a", "b", "c", "d"]
# if "z" in letters:
#     print(letters.index("z"))
# else:
#     print("Item does not exist in the list")
    
# There is another method that you might find useful
# The count() method
# The coun() method will return the number of occurences of a given item in the list

letters = ["a", "b", "a", "c", "a", "d", "a"]
print(letters.count("a"))