# There are times that we need to compare two objects

# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
# first = Point(1, 2)
# print(first)
# second = Point(1, 2)
# print(second)

# print(first == second)

# The result will be "False" because th equality operator "==" 
# compares the references or addresses of the two objects in memory

# *** How do we solve this problem?
# To solve this problem we use MAGIC METHOD
# The magic method we will use is called when we compare two objects

# Go to the page - https://rszalski.github.io/magicmethods/ and look for "Comparison magic methods"
# You will see all the magic methods we have for comparing; For example, we have:
# __eq__ - for equality
# __ne__ - for inequality
# __lt__ - for less-than
# and so on ...

# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __eq__(self, second):
#         return self.x == second.x and self.y == second.y
    
    
# first = Point(1, 2)
# second = Point(1, 2)

# print(first == second)

# print(first > second) # This will fail...

# ***************
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, second):
        return self.x == second.x and self.y == second.y
    
    def __gt__(self, second):
        return self.x > second.x and self.y > second.y
    
    def __ge__(self, second):
        return self.x >= second.x and self.y >= second.y
    
    
    
first = Point(1, 2)
second = Point(1, 2)

print(first == second)
print(first > second)
print(first < second)

# What if we want to use ">=" and "<=" instead?
# Will this work?

print(first >= second)
print(first <= second)

third = Point(10, 20)
fourth = Point(1, 2)

print(third == fourth)
print(third >= fourth)