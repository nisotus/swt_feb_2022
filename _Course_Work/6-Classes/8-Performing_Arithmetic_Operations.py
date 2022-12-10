# We also have MAGIC METHODS for performing arithmetic operations between two objects

# *** Code that will fail
# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# first = Point(10, 20)
# second = Point(1, 2)
# print(first + second)

# How do we solve this? We can use magic method

# ***************************************
# Go to the page - https://rszalski.github.io/magicmethods/ and look for "Numeric magic methods"
# If you scroll down, you will see "Normal arithmetic operators"
# __add__ - For addition
# __sub__ - For subtraction
# __mul__ - For miltiplication
# and so on ...

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        # return self.x + other.x, self.y + other.y
         return Point(self.x + other.x, self.y + other.y)

first = Point(10, 20)
second = Point(1, 2)
combined = first + second
# print(combined.x)
# print(combined.y)
# print(first + second)

print(combined.x + combined.y)