# There are times that you want to import modules from sibling packages
# For example, let us add a sub-package called "customer" under package "eCommerce"

# In the package "customer" we create a module "contact" to keep our customer contacts

# Now, lets say in our "sales3" module, under "shopping" package
# We want to use the "contact" module in the customer package

# So how do we do this?

# To import a module from another package, we can use an ABSOLUTE or RELATIVE import statement

# *** ABSOLUTE IMPORT STATEMENT
from eCommerce.customer import contact
contact.customer_contact()


# *** RELATIVE IMPORT STATEMENT
# from . - Using one dot "." represents the current package
# from .. - Using two dots ".." takes us one level up


# *** Best Practise
# A a best practise, use ABOLUTE imports -. Thats what PEP8 recommends
# But when your absolute imports get really verbose like a.b.c.d.e.
# Then you might be able to simplify the import statement by using a RELATIVE import

