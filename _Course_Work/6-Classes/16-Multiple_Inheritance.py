# In Python, a class can have multiple base classes
# In the example below, we have a "Manager" class that has two base classes "Employee" and "Person"
# This is what we call "MULTIPLE INHERITANCE" and similar to multi-level inheritance
# It is a source of issues if you don't use it properly

class Employee:
    pass


class Person:
    pass


class Manager(Employee, Person):
    pass


# Let's take a look at an example below:
# Let's define two "greet" methods in both "Employee" and "Person" classes

class Employee:
    def greet(self):
        print("Employee Greet")

class Person:
    def greet(self):
        print("Person Greet")
        
class Manager(Employee, Person):
    pass

# So what will happen if we create a "Manager" object and call the "greet" method?
# Which "greet" method is going to get called?

manager = Manager()
manager.greet()

# When we run the program, we notice that the "greet" method in the "Employee" class gets called
# Why is this?

# This is because we added the "Employee" class first - "class Manager(Employee, Person)"

# When Python Interpreter tries to execute the code - "manager.greet()"
# First is looks at the "Manager" class to see if it has a the "greet" method
# If it doesn't, it will look at it's first base class "Employee" in this case
# If "Employee" class does not have the "greet" method, then it will look at "Person" class

# **** Why is this an issue?
# If in the future another programer joins the team and for some reason
# They decide to change the order of the base classes, our program will have a different behaviour

class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Person, Employee):
    pass


manager = Manager()
manager.greet()

# *****************************
# So if multiple inheritance is a bad thing, why does Python support it?
# *****************************

# *****************************
# So if multiple inheritance is a bad thing, why does Python support it?
# Multiple inheritance is not always a bad thing. It is bad when you don't use it properly

# If the classes are small classes and have absolutely nothing in common
# and you want to inherit their features in a separate class,
# then it's perfectly fine to use multiple inheritance

# Things start to get complicated when the classes have things in common
# like the "greet" method in our example.

# *** A good example of multiple inheritance

class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass

# As you can see, the two classes "Flyer" and "Swimmer" are very small and abstract
# They have nothing in common

# So we can combine the features of these two classes into one = "FlyingFish"
# Meaning a "FlyingFish" that knows how to fly and how to swim


class FlyingFish(Flyer, Swimmer):
    pass

# This is a good example of multiple inheritance
