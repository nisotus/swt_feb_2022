# LAMBDA EXPRESSIONS or LAMBDA FUNCTIONS

# A simple one line anonymous function that we can pass to other functions

# Let's take an example

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

# IMPROVEMENT
# We can improve this code and make it cleaner by using a LAMBDA EXPRESSION or an ANONYMOUS FUNCTION
# So we don't have to define the function first and then pass it as a reference

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

items.sort(key=lambda item:item[1])
print(items)

# The syntax for writing a lambda function is (key=lambda parameters:expression)
# using the syntax above we can rewrite the function below:

def sort_item(item):
    return item[1]

# As:
items.sort(key=lambda item:item[1])

# Breaking it down
# How many parameters do we have in the function sort_item(item) ?
# Ony 1 parameter and the parameter is "item"
# So that means that our (key=lambda parameters:expression) = (key=lambda item:item[1])

# So the final solution using Lamda function is below:

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

items.sort(key=lambda item:item[1])
print(items)


# Now you can see with this syntax, we don't need to define any function
# So using the Lambda function is a shorter and cleaner way to define a function
# that we are going to use only once as an argument to another function

#******************************

shopping_cart = [
    ("Clipper", 1),
    ("Brush", 20),
    ("Laptop", 2)
    ("Pen", 150),
    ("USB-Type-C", 51),
    ("Jabra-Headset", 1000)
]

