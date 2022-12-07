# Define a new class called Person
# The "person" objects should have a name attribute as well as a talk method
# Create a Person object called "Jogn Smith" from class "Person"
# Call the talk method for object "John Smith" and "John Smith" should say - "Hi, my name is "name", and the weather is nice today"

# Now I want you to create another Person object called "bob" from class "Person"
# Give the name "Bob Smith"
# Call the talk() METHOD for object "bob" and "bob" should say - "Hi, my name is "name", and the weather is not nice today"

class Person:
    def __init__(self, name, words):
        self.name = name
        self.words = words 
           
    def talk(self):
        print(f"My name is {self.name}, {self.words}")
        
    def talk2(self):
        print(f"My name is {self.name}, {self.words}")

    def talk3(self):
        print(f"My name is {self.name}, {self.words}")
        
john = Person("John Smith", "and the weather is nice today")
john.talk()

bob = Person("Bob", "and the weather is not nice today")
bob.talk()

print(bob.words)
print(john.name)