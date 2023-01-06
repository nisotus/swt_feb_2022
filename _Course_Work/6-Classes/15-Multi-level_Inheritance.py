# We have seen that inheritance is a good thing
# It prevents code duplication and allows us to reuse code

class Animal():
    def eat(self):
        print("eat")
        
    def walk(self):
        print("walk")
        
class Bird(Animal): # We are reusing/inheriting the "eat" and "walk" methods from the "Animal" class
    def fly(self):
        print("fly")
        
# A chicken is a bird, so we can inherit it from the "Bird" class

class Chicken(Bird):
    pass

# Now, there is a problem in the program above

# *** What is the problem???

# The issue here is that *chickens cannot fly*
# This is an example of inheritance abuse

#*****
# Another example is the employee example: Employee -> Person -> LivingCreature -> Thing

# Because a perosn is a living creature in the real world
# does not mean you should have classes like that in your software

# The methods you add in your classes are there to solve a business problem
# That should be the focus of your software

# So just because an animal can eat in the real world,
# doesn't mean your "Animal" class should also have the "eat" method

# So avoid MULTI-LEVEL INHERITANCE at all times
# If you want to use inheritance, limit it to one or two levels
# Going beyond that, you are going to shoot yourself in the foot