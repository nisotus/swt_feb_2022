# In this session we are going to look at the powerful built-in function called "dir"
# With the "dir" function, we can get a list of ATTRIBUTES and METHODS defined in an object

# Let's import the "sales3" module from the "shopping" package

from eCommerce.shopping import sales3

# Now "sales3" is an object and we can use the dot operator "."
# To access all the attributes and methods defined in the object "sales3"

# As you work on large projects, there are times that things don't work like you expect
# So you can use the "dir" function for debugging

# Let's see an example:

# print(dir("sales3"))

# When we run the program, we get an array of strings
# In the array, we have all the attributes and methods defined in the "sales3" object

# When we run the program, we get an array of strings
# In the array, we have all the attributes and methods defined in the "sales3" object

# So we get the methods/funtions that we have created
# As well as some magic methods that were automatically created by Python

# Let's take a look at some of the magic methods

print(sales3.__name__)  # This returns the name of our module
print(sales3.__package__) # This returns the name of the package
print(sales3.__file__) # This returns the name of the file including the file system path