# Read about LIST, TUPLE, ARRAY, SET and DICTIONARY in Python
# Create a LIST
# Create a TUPLE
# Create an ARRAY
# Create a SET
# Create a DICTIONARY

# A print each of them out to the terminal


#create a list
my_list= [1,2,3, "a", "b", "c","jessica",True]
print(my_list)

my_tuple = (1,2,3, "a", "b", "c","jessica",True)
print(my_tuple)

#create a tuple from a list
my_list= [1,2,3,4,5, "a", "b", "c","jessica",True]
my_tuple = tuple(my_list)
print(my_tuple)

#to create an array.
from array import array
from sre_constants import FAILURE
my_list =[1 ,2 ,3 ,4 ,5 ,6]
my_array = array("i" ,[1 ,2 ,3 ,4 ,5 ,6])
print(my_array)
my_array.append(2)
print(my_array)

# To create a Set
my_list =[1 ,2 ,3 ,4 ,5 ,6]
my_set =set(my_list)
print (my_set)

#create a new list that has duplicates elements
new_list =[1 ,2 ,2 ,3 ,4 ,5 , 5 ,6]
new_set = set(new_list)
print (new_set)

new_set.remove(1)
print(new_set)

my_dictionary=("name : Jessica",
"Sex : Female",
"complextion : fair",
"city : MalmÖ")

print(my_dictionary)



    
    

