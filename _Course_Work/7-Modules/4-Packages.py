# As our application grows and we have so many modules
# We probably want to organize our modules into sub-directories
# Otherwise we will end up with hundreds or thousand of Python files/modules in one folder

# If we try to import a module that does not exist in a current directory,
# the "import" statement will have a "red underline"

import sales2


# If we want to import a module that exist in another directory,
# We need to create a file called "__init__.py" under the directory
# When we add the "__init__.py" file, Python will treat the directory/folder as a "PACKAGE"

# So a package is a container for one or more modules
# In file system terms, a PACKAGE is mapped to a DIRECTORY, a MODULE is mapped to a FILE

# So if we want to import a module from a package, we have to prefix the module name with the package name

import eCommerce.sales2

eCommerce.sales2.calc_shipping
eCommerce.sales2.calc_tax

# Obviously this will make our code a little bit noisy
# because everytime we want to us the objects in the "sales2" module
# we'll have to type "eCommerce.sales2" - This is tedious

# A better approach is to use the "from" statement

from eCommerce.sales2 import calc_tax, calc_shipping

calc_shipping()
calc_tax()


# We can also import the module from the package like below:

from eCommerce import sales2

# Then we can use the dot operator "." to access all the members of the module "sales2"

sales2.calc_tax
sales2.calc_shipping