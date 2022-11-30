# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point(1, 2)
# point.draw()


# We don't have to define all the attributes in the constructor
# This is because objects in Python are dynmaic, similar to JavaScript

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, {self.y}, {self.z})")


# point = Point(1, 2)
# point.z = 20
# point.draw()

# ***Instance Attributes

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point(1, 2)
# point.draw()

# another = Point(3, 4)
# another.draw()

# **** Class Attributes
# As a metaphor, we can say all humans have two eyes and two ears
# They are shared across all instances

class Point:
    default_color = "red"
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

Point.default_color = "Yellow"


point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
point.draw()

another = Point(3, 4)
print(another.default_color)
another.draw()


# *** To Recap
# Class level attributes are shared across all instances of a class
# If you change their value, the change is visible to all objects of that type

# In practical terms, you will be using instance attributes most of the time
# But there are times that you may want to define a class level attribute
# that is shared across all objects of a given type.