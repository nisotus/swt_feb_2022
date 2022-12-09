# Define a new class called Person
# The "person" objects should have a name attribute as well as a talk method
# Craete a Person object called "Jogn Smith" form class "Person"
# Call the talk method for object "John Smith" and "John Smith" should say - "Hi, my name is "name", and the weather is nice today"

# Now I want you to create another Person object called "bob" from class "Person"
# Give the name "Bob Smith"
# Call the talk() METHOD for object "bob" and "bob" should say - "Hi, my name is "name", and the weather is not nice today"


###solution################
class Pearson:
    def __init__(self, name, word):
        self.name = name
        self.word = word
        

        
    def talk(self):
        print(f"My name is {self.name}, {self.word}")

    
    
    
    
john = Pearson("dunni",  "and the weather is nice today" )
bob = Pearson("dunni", "and the weather is not nice today")
john.talk()
# print(john.name)
#print("hi, my name is ", john.name, john.talkmethod, "today")
bob.talk()
