# In the example below, our "Animal" class has a constructor "__init__"
# Where we initialize the age attribute to "1"

# class Animal():
#     def __init__(self):
#         self.age = 1

#     def eat(self):
#         print("eat")


# class Mammal(Animal):
#     def walk(self):
#         print("walk")
        
# m = Mammal()

# What if we want to add a constructor to the "Mammal" class, and initialize it's weight to the value "2"
# How do we do this?


# class Animal():
#     def __init__(self):
#         self.age = 1

#     def eat(self):
#         print("eat")


# class Mammal(Animal):
#     def __init__(self):
#         self.weight = 2
        
#     def walk(self):
#         print("walk")
        
# m = Mammal()

# a = Animal()

# Below code will pass
# print(a.age)
# print(m.weight)

# Below will fail
#print(m.age) # We get - AttributeError: 'Mammal' object has no attribute 'age'

# The reason this happened is because the constructor "__init__" in the "Animal" class was not executed

# The contructor that we defined in the "Mammal" class replaced the constructor in the base "Animal" class
# This is what we call "METHOD OVERRIDING"

# So we are overriding or replacing a method in the base class

# **********************************

# Now, what if you still want to execute the constructor in the base class and initialize the age of an animal?

# To do this, we edit the "Mammal" class with the built-in "super" function
# To get access to the super or base class = "Animal" in this case


class Animal():
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        self.weight = 2
        super().__init__()
        
    def walk(self):
        print("walk")
        
m = Mammal()

print(m.age)
print(m.weight)

# We can also change the order of the method calls
# Let's try to call the constructor or the "Animal" after we initialize a "Mammal" object
  
# *** To Recap
# Method overriding means replacing or extending a method defined in the base class
# In our example, we are extending the "__init__" method that we defined in the "Animal" class

# In the "Mammal" class, we call the contructor of the "Animal" class using - "super().__init__()"
# If we remove the line - "super().__init__()" the implementation we have in the "Mammal" class
# Will completely replace the "__init__" method in the "Animal" class