# In the last session we defined the "Animal" class
# and created the "Mammal" object "m"

class Animal:
    def eat(self):
        print("eat")
        
class Mammal(Animal):
    def walk(self):
        print("walk")
        
class Fish(Animal):
    def swim(self):
        print("swim")
        
m = Mammal()

# Now let's have a look at a couple of useful built-in functions

# *** isinstance()
# "isinstance()" tells us if an object is an instance of a given class
print(isinstance(m, Mammal))

print(isinstance(m, Animal))

# *** Something interesting
# The "Animal" class inherits from another class called "object"
# Eventhough we did not add it - "class Animal(object)"

# So we have a class called "object" - and that is the base class for all classes in Python
# Every class that we have directly or indirectly derives from the "object" class

class Animal(object):
    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()

# **************************
# So let's have a look
class Animal():
    def eat(self):
        print("eat")

class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()

print(isinstance(m, object))

# *** Built-in function for creating an empty object
class Animal():
    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
o = object()

# Using "o." you will see all the magic methods that every class in Python has
# Using "m." you will also see all the magic methods that every class in Python has


# *** issubclass()
# "issubclass()" - With this you can see if a class derives from another class
class Animal():
    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")
        
m = Mammal()
print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))
print(issubclass(Animal, object))
print(issubclass(object, Animal))