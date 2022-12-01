# So we have "Instance Methods" as well as "Class Methods"

# *** Instance Methods
# Both the methods "__init__()" and "draw()" that we defined below are instance methods

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")
        
# So we can call them using an instance of the "Point" class, like below:

# point = Point(1, 2)
# point.draw()

# *** Class Methods
# Let's say in our program, we want to create a a point, with initial values "(0, 0)"
# We can create it like below:

# point = Point(0, 0) 

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")

# point = Point(0, 0)
# point.draw()

# However, there is a different way to create a "point" object with the values "(0, 0)"
# Using a class reference "Point.zero()"

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)
    
    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point.zero()
point.draw()