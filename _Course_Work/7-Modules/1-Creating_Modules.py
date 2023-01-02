# A module is a file that contains some Python code

# *** Here is the question?
# How do we decide what functions or what classes we should put in what modules?

# Let's take the supermarket as an example - In a supermarket,
# Each sections contains highly related products, you don't see cleaning products in the fruit section

# By the same token, a module should contain highly related objects
# These objects can be Functions, Classes, Variables and so on

# Let's have a look at an example below:
# The two functions are highly related to the concept of sales

# def calc_tax():
#     pass

# def calc_shipping():
#     pass

# *** Importing Modules
# There are a couple of ways to import modules

# *** Approach 1 - Importing a single object from another module
# from module import object

# When using the "from" statement, pressing "Ctrl + Space" after the "import" statement
# Will show all the objects defined in the module, you will also see a bunch of modules
# That Python automatically creates - We will look at this later

from sales import calc_shipping

from sales import calc_tax

# Now we can call the calc_shipping function, just like a function we have defined in the current module

calc_shipping()
calc_tax()

# *** Approach 2 - Importing multiple objects from another module

# To import multiple objects from a module, you can seperate them using a comma (,)
from sales import calc_shipping, calc_tax

calc_shipping()
calc_tax()

# *** Approach 3 - Importing multiple objects from another module using asterisk "*"
# There are some tutorials out there that teach you a shortcut to import multiple objects using an asterisk "*"
# While this makes your code shorter, it is actually a bad practise, because in the module
# You could have several different functions or variables and if you blindly import them into the current module
# Some of those objects may overwrite the objects with the same name in the current module
# So don't import all objects using "*", only import the stuff that you need.

# *** Approach 4
# There is also another way to import a module
# Instead of starting with "from" you start with "import" and then you add the name of the module

import sales

# Now in this module we have an object called sales
# and we can use the dot operator "." to access it's members

sales.calc_tax()
sales.calc_shipping()

# So "calc_shipping" and "calc_tax" functions are now a method of the object "sales"

# *** To Recap
# So basically, you can either import the entire module as an object
# Or you can import specific objects from the module

# The approach you choose is purely your personal preference
# There is no right or wrong here, there is not even a performance difference
# Whenever we want to import one object from a module, that entire module needs to be loaded
# Then we can pick one object or every object from the module