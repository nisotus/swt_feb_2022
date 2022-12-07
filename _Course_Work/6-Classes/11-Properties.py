# There are times you want to have control over the attributes/properties in a class

# For example:

# Let's say we have a "Product" class
# In the CONSTRUCTOR of class "Product" we can set the "price" attribute

# class Product:
#     def __init__(self, price):
#         self.price = price
        
# Let's you have people working in a warehouse and they want to set teh price for the product
# Now, someone makes a mistake and set a negative price.

# product1 = Product(-50)

# *** This is not good!!!
# How can we prevent/ensure that our product does not ahev a negative price?

# *** Solution 1
# we can make the attribute "price" private
# we also need tod efine a method to get and set the price

# class Product:
#     def __init__(self, price):
#         self.set_price(price)
        
#     # Method for getting price
#     def get_price(self):
#         return self.__price

#     # Method for setting price
#     def set_price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative")    
#         self.__price = value
    
# product1 = Product(50)
# print(product1.set_price(-50))

# *** Solution 1 is simple, but very ugly. It is not Pythonic.

# *** Solution 2
# Using the "PROPERTY" object
# A property is an object that sits in front of an attribute
# and allows us to "get" or "set" the value of the attribute

# The property function takes four parameters and all of them are optional

# "fget" - A function for getting the value of an attribute
# "fset" - A function for setting the value of an attribute
# "fdel" - A function for deleting an attribute
# "doc" - For documentation 

# In our case, we need to supply two arguments "get_price" and "set_price"
# You should not call the methods like - "get_price()" and "set_price()"
# Simply pass a reference to them like "get_price" and "set_price"

# class Product:
#     def __init__(self, price):
#         self.set_price(price)
        
#     # Method for getting price
#     def get_price(self):
#         return self.__price

#     # Method for setting price
#     def set_price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative")    
#         self.__price = value
    
#     price = property(get_price, set_price)
    
# product1 = Product(10)
# print(product1.price)
# product1.price = -1
# print(product1.price)

# We want our objects or classes to be the same
# We want them to have minimal number of functions or methods exposed to the outside
# *************
# *** Solution A
# Make the methdos set_price and get_price private methods
# by using undersore "__set_price" and "__get_price"
# this will add more noise

# class Product:
#     def __init__(self, price):
#         self.__set_price(price)
        
#     # Method for getting price
#     def __get_price(self):
#         return self.__price

#     # Method for setting price
#     def __set_price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative")    
#         self.__price = value
    
#     price = property(__get_price, __set_price)
    
# product1 = Product(10)
# print(product1.price)
# product1.price = -1
# print(product1.price)

# *** Solution B
# A better, cleaner and shorter way to achieve the same result
# Is to use a DECORATOR. Earlier we used a decorator calles "@classmethod"
# To convert an instance method to a class method

class Product:
    def __init__(self, price):
        self.set_price(price)

    # Method for getting price
    @property
    def price(self):
        return self.__price

    # Method for setting price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


product = Product(10)
product.price = -1
print(product.price)