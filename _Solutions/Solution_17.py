# Write a program to remove the duplicates in a list
# duplicate = [8, 6, 4, 9, 10, 7, 12, 7, 30, 7, 8, 10, 1, 10, 12, 13, 8, 7]

# Use a function to write thesame code

# duplicate = [8, 6, 4, 9, 10, 7, 12, 7, 30, 7, 8, 10, 1, 10, 12, 13, 8, 7]

# def unique():
#     duplicate = [8, 6, 4, 9, 10, 7, 12, 7, 30, 7, 8, 10, 1, 10, 12, 13, 8, 7]
#     unique = list(dict.fromkeys(duplicate))
#     return unique

# print(unique())

#*********************************************

# def my_unique_list():
#     duplicate = [8, 6, 4, 9, 10, 7, 12, 7, 30, 7, 8, 10, 1, 10, 12, 13, 8, 7]
#     print("List Before removing duplicates: ", duplicate)
#     temp_list = []
    
#     for i in duplicate:
#         if i not in temp_list:
#             temp_list.append(i)
    
#     return temp_list

# print("My unique list is:", my_unique_list())

#*******************************************

duplicate = [8, 6, 4, 9, 10, 7, 12, 7, 30, 7, 8, 10, 1, 10, 12, 13, 8, 7]
uniq = list(set(duplicate))
print(uniq)
