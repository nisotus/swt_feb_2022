# Read about LIST, TUPLE, ARRAY, SET and DICTIONARY in Python
# Create a LIST
# Create a TUPLE
# Create an ARRAY
# Create a SET
# Create a DICTIONARY

# A print each of them out to the terminal

#Code
#Create a list

my_list = [1,2,3, "a", "b", "c", "dunni", True]
print(my_list)

# #To create a Tuple

my_tuple = (1,2,3,4,5,6,"a", "b", "c", "dunni", True)
print(my_tuple)

#or we create a tuple from a list
my_list = [1,2,3, "a", "b", "c", "dunni", True]
my_tuple = tuple(my_list)
print(my_tuple)


# To create an array

from array import array

my_list = [1, 2, 3, 4, 5, 6, 7]

my_array = array("i",[1, 2, 3, 4, 5, 6, 7])
print(my_array)
my_array.append(2)
print(my_array)


#To create a set

#We can create set from my list

my_list = [1, 2, 3, 4, 5, 6, 7]
my_set = set(my_list)
print(my_set)

#0r create a new list that has duplicate elements
new_list = [1, 1, 2, 2, 2, 3, 4, 4, 4, 5]
new_set = set(new_list)
print(new_set)

new_set.remove(5)
print(new_set)


#To create a dictionary
my_dictionary = {
    "name":"Dunni",
    "height": "tall",
    "complexion": "dark",
    "city":"Gothenburg"
}
print(my_dictionary)







