# Currently in the "sales4" module, we have defined two functions "calc_shipping" and "calc_tax"

# def calc_tax():
#     pass


# def calc_shipping():
#     pass

# Now, we can also write any additional statements and these statements will be executed
# The first time the module "sales4" is loaded

# So if we import "sales4" module in a few different modules in our program
# Python will load the "sales4" module only once and then cache it in memory

# So any statements we write in the "sales4" module will be executed once

# As an example, let's add the code *print("Sales4 Initialized")* in the "sales4" module
# Now go to "app1" module and import "sales4"

# *** In VC Code, to quickly look up a file
# Press "Control + P" on Windows or "Cmd + P" on Mac

# Now run "app1.py"
# You will get the result - "Sales4 Initialized" printed to the terminal

# Using this technique we can write the initialization code for our packages
# To do this, go to the "__init__.py" file under the "ecommerce" package
# Add the code - *print("Ecommerce Initialized")*

# Now go to "app1" module and run the program again
# You should get the results: "Ecommerce Initialized" and "Sales4 Initialized"
# Meaning our "ecommerce" package was first initilaized and then the "sales4" module

# *** Now let's take this to the next level
# Go to "sales4" module and print the name of the module
# By passing the "__name__" attribute to the print function

# Save the changes and go back to "app1" module and run the program
# You get the name of the module - "ecommerce.shopping.sales4" and other objects passed to the print function

# However, if we go to "sales4.py" and run the program
# The name of the module is changed to "__main__"

# *** Important
# The name of the module that starts our program is always "main"

# Now we can do something interesting
# Create another module called "sales5.py" under package "ecommerce"
# Copy the two functions in "sales4.py" into "sales5.py" - make sure you don't add the "print" function

# After we define the two functions in "sales5"
# Add below code

# if __name__ == "main":
#     print("Sales5 Started")
#     calc_tax()

# With the code below:

# if __name__ == "main":
#     print("Sales5 Started")
#     calc_tax()

# we can make "sales5" useable as a script as well as a reusable module that we can import into another module

# So if we run the "sales5" file directly, the name of the module will be "main"
# And below *if __name__ == "main":* we can have any initialization code
# Or we can call one of the existing functions in the module, like "calc_tax" or "calc_shipping"

# However, if we import the "sales5" module into another module
# The code below will not be executed

#     print("Sales5 Started")
#     calc_tax()

# Bescause at that point, the name of the "sales5" module will not be "main"
# It will be "ecommerce.shopping.sales5"
