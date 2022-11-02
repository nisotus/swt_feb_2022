# Write a program to remove the duplicates in a list
duplicate = [8, 6, 4, 9, 10, 7, 12, 7, 30, 7, 8, 10, 1, 10, 12, 13, 8, 7]

# Use a function to write thesame code

mylist = [8, 6, 4, 9, 10, 7, 12, 7, 30, 7, 8, 10, 1, 10, 12, 13, 8, 7]

mylist = (dict.fromkeys(mylist))
print(mylist)