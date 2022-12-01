# Magic methods have two underscores at teh beginning and end of their names
# For example "__init__()" method, we don't directly call it
# It is automatically called by the Python Interpreter when we create a new object

# Let's take a look at below class:

# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")

# point = Point(1, 2)

# point.draw()

# If you want to see the complete list of magic methods in Python 3
# Follow the link: https://rszalski.github.io/magicmethods/

# Lets us take "__str__" as an example
# Let's say we print the "point" object to the terminal using "print(point)"

# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")

# point = Point(1, 2)
# print(point) # This will give us "<__main__.Point object at 0x000001EE9AB27D60>"

# "__main__" is the name of the MODULE
# "Point" is the name of the CLASS
# "0x0000020AC204B070" is the ADDRESS of the "point" object in MEMORY

# **** Let us look at the "__str__()" magic method
# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")

# point = Point(1, 2)
# point.__str__()
# print(point)

#****************

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    # def draw(self):
    #     print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(str(point))
