# Let's see how to create a "Point" class in Python

# *** Note that - Unlike VARIABLES and FUNCTIONS
# *** We use PASCAL naming convention when naming CLASSES
# *** Capitalize first letter of every word
# *** Don't use underscore (_) to separate multiple words


# In the class block, we define all the functions related to the class
# All functions in our classes should have at least one parameter
# By convention, we call that parameter "self" - We will talk more about "self"

class Point:
    def draw(self):
        print("draw")
    
    def move(self):
        print("move")
        
# Now we have a BLUEPRINT for creating "Point" objects

# To create a "Point" object, we call the class "Point" like a function
# Calling class "Point" like a function "Point()" will return a "Point" object
# Then we can assign it to a variable

point = Point()

# Now if we use the dot "." operator, you can see we have the "draw" and "move" methods
# as well as a bunch of other methods that we didn't define

print(type(point))

# We will get a calss of __main__.Point - <class '__main__.Point'>
# The "__main__" is the name of our module and we will look at that later

# We have another useful function called "isinstance(o, t)"
# The function "isinstance" can be used to check if an object is an instance of a given class
# For example

print(isinstance(point, int))

print(isinstance(point, Point))


# So this is how we create custom classes in Python
# But our "point" object need some initial values like "x" and "y"
# To set these values, we need a CONSTRUCTOR - This is the topic for the next session