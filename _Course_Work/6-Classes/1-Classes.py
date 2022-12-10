# CLASSES are extremely important in Python and in programming in general

numbers = [1, 2, 3]

print(type(numbers))

# Now we have learnt that when we use the dot "." notation - like "numbers."
# We get access to functions/methods that are available for list object which is in this case "numbers"

# How about we create an object like "shopping_cart"
# and the "shopping_cart" object would have methods like below:
#***********
#"shopping_cart.add()"
#"shopping_cart.remove()"
#"shopping_cart.get_total()"

# Or as another example, let's say we have a "point" object
# The "point" object has methods like below:
#***********
#"point.draw()"
#"point.move()"
#"point.get_distance()"
#"point.get_distance(1, 2)"

# Or as another example, let's say we have a "car" object
# The "car" object has methods like below:
#***********
#"car.start()"
#"point.drive()"
#"point.stop()"
#"point.change_speed()"

#**********This is where CLASSES come to our rescue*******#

# *** What is a CLASS
# A class is a BLUEPRINT for creating NEW OBJECTS

# *** How to check the class of objects in Python
x = 1
print(type(x))

# So in Python, we have a class of "int" for creating integer objects
# Similarly we have classes for creating strings, booleans, lists, dictionaries, etc.
 
# Every object we have in Python is created using a CLASS
# The CLASS is a blueprint for creating objects of that TYPE/CLASS

# For example:
# We could have a class called "Human"
# The "Human" class will define all the ATTRIBUTES of HUMAN

# Then we could create objects like: John, Mary, Smith, Peter

