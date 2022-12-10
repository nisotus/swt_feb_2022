class Mammal:
    # All mammals should be able to eat, so we define a "eat" function/method
    def eat(self):
        print("eat")
        
    # All mammals should be able to walk, so we define a "walk" function/method
    def walk(self):
        print("walk")
        
    # All mammals should be able to smell, so we define a "smell" function/method
    def smell(self):
        print("smell")

    
class Fish:
    # All fish should be able to eat, so we define a "eat" function/method
    def eat(self):
        print("eat")
        
    # All fish should be able to swim, so we define a "swim" function/method
    def swim(self):
        print("swim")
        
# As you can see, we have duplicated the "eat" method in both "Mammal" and "Fish" classes
# We have the concept called DRY = DON'T REPEAT YOURSELF

# So how do we solve this problem? We have two solutions
# INHERITANCE
# COMPOSITION

# *** Inheritance Solution
# Inheritance is a mechanism that allows us to define the common behavior
# or common functions in one class and then inherit them in other classes

# Here is how it works:

# Define a seperate class called "Animal" and move the "eat" method to class "Animal"


class Animal:
    def eat(self):
        print("eat")

# How do we implement the "Mammal" class to inherit the "eat" method from the "Animal" class

# We simply pass the "Animal" class as parameter to the "Mammal" class

class Mammal(Animal):
    def walk(self):
        print("walk")
        
    def smell(self):
        print("smell")

# "Animal" is the parent or Base class
# "Mammal" is the Child or Sub class

# We can apply the same concept to the "Fish" class

class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
f = Fish()

m.eat()
m.smell()
m.walk()

f.eat()
f.swim()

# ** INHERITANCE is not limited to methods
# We can also inherit the attribites of a base class

# For example, we go back to the "Animal" class
# Define a constructor "def __init__"
# In the constructor, set "age = 1"

class Animal:
    def __init__(self, age):
        self.age = age
    
    def eat(self):
        print("eat")
        
class Mammal(Animal):
    def walk(self):
        print("walk")
        
class Fish(Animal):
    def swim(self):
        print("swim")

m = Mammal(1)
print(m.age)

# So this is the basic of INHERITANCE
# In real programs, we don't build Animals or Mammals or Fish, unless we are building a game
# We use these examples, just to simplify the explanation

# Later we are going to see a real world example of inheritance in our programs