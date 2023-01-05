# In this file we are importing the "sales" module

import sales

# When Python sees this, it will look for a file called "sales.py" in the current directory
# If it does not find the file, it will look in a bunch PREDEFINED DIRECTORIES that come with Python installation

# Let's have a look:

# We have a built-in object called "path", let's import it the "sys" modlue that holds the "path" object

import sys

# In "sys" module, we have a variable called path
# Which returns the list of directories that Python will look at to find a module

sys.path

# let's print "sys.path" to the terminal

print(sys.path)

# You will get an array of strings, it will be different on your machine depending on your OS
# So when Python sees and "import" statement, it will search all the listed directories to find the module
# As soon as it finds the module, the search stops there

# ***Question
# How do we import a module from a SUB-DIRECTORY?
# To do this we need to look at PACKAGES - This is the next topic