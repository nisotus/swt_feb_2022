# As our program grows, we may want to break down a package into sub-packages
# For example, let's imagine our ecommerce package has a sub-folder called "shopping"

# Create a new file called "sales3" and move it to the folder "shopping"

# Currently, shopping is a folder, not a package, because it does not contain the "__init__.py" file
# So, lets add the "__init__.py" file to the "shopping" folder

# How do we import the module "sales3" into our program?

from eCommerce.shopping import sales3

