# Write a Python program using classes to create attributes and behaviours for different Animals
# Create a base class called "Animal"
# Make sure to show in your code that your "Animal" class inherits attributes and behaviour from the "Object" class
# The "Animal" class should have the attributes: Eyes, Head, Ears, Nose, Legs,

# The "Animal" class should have behaviours: Walk, Run, Eat, Jump, Swim, Cry, Sleep, Slither, Crawl, Bark, Roar, Hiss

# Create additinal classes of animals including: Lion, Shark, Goat, Frog, Snake, Lizard, Dog

# Think about how you can create the subclasses by category
# For example, we know that fishes can swim and Dogs can bark, so create the sub classes to capture all attributes ad behaviours above

# Make sure you don't leave any attribute or behaviour out of your implimentation.



#   SOLUTIONS
class Animal:
    def __init__(self, eyes ,head ,ears ,nose ,legs ):
        self.eyes= eyes
        self.head=head
        self.ears=ears
        self.nose=nose
        self.legs=legs


class Animal:
    def Walk(self):
        print("Walk")
    def Run(self):
        print("Run")
    def Eat(self):
        print("Eat")
    def Jump(self):
        print("jump")
    def Cry(self):
        print("Cry")
    def Sleep(self):
        print("sleep")

class Lion(Animal):
    def roar(self):
        print("roar")
    
class shark(Animal):
    def swim(self):
        print("swim")

class goat(Animal):
    def  eat(self):
        print("eat")

class frog(Animal):
    def jump(self):
        print("jump")

class snake(Animal):
    def slither(self):
        print("slither")
    def Hiss(self):
        print("hiss")

class lizard(Animal):
    def crawl(self):
        print("crawl")

A=Animal
s=snake
L=Lion
f=frog
s=shark
g=goat
l=lizard



A.Eat()
A.run()
A.walk()
A.sleep()
A.jump()

s.swim()





