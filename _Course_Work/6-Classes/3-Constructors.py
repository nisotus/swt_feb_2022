# class Point:
#     def draw(self):
#         print("draw")


# point = Point()

# print(type(point))

# If we want to supplu initial values for example coordinates "x" and "y" like "point = Point(1, 2)"

# We cannot supply these values like below:
# point = Point(1, 2) # This will not work...

# To achieve this we need a CONSTRUCTOR
# A CONSTRUCTOR is a special method that is called when we create a new "point" object

# *** Creating a CONSTUCTOR
# __init__(self) like this - "def __init__(self)"
# "__init__" is a special method that we call MAGIC method

# As parameters to the magic method "__init__", we add "self"
# Any otehr paremters for initiating the object can also be added

class Point:
    def __init__(self,x, y, z):
        self.x = x # This can be any value like 0 or the "x" argument that we receive in the method
        self.y = y # This can be any value like 0 or the "y" argument that we receive in the method
        self.z = z
    
    def draw(self):
        # print("draw")
        print(f"Point({self.x}, {self.y}, {self.z})")
        
point = Point(1, 2, 3)

# Now when we use the dot "." operator on the "point" object, we can access the attributes "x" and "y"
# point.x
# point.y

# We can simply now print the value of "x" and "y"

# print(point.x)
# print(point.y)
point.draw()


# *** To Recap
# The methods that you have in a class should have at least one parameter, which by convention is called "self"

# "self" references the current object we are working with

# when calling methods of an object, we never have to supply a value for the "self" parameter
# Python Interpreter does that for us.

# As a metaphor, think of a human being
# The human can have attributes like eye color, height, weight and so on,
# As well as functions like walk, talk, run and so on...

# So in the "Point" class, the attributes are "x" and "y" parameters
# While the functions are defined within the class 


