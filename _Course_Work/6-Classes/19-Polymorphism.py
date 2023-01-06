# In the last session we learnt about "Abstract Base Classes"
# As another example below, we have defined an abstract base class

from abc import ABC, abstractmethod

# We define an abstract base class called "UIControl"
# This class has an abstract method called "draw" and the "draw" method has no implememtation
# So the class "UIControl" only defines the contract or the interface
# that all it's derivatives or children should follow

# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass
    
# Below we have two classes "TextBox" and "DropDownList" that derive from class "UIControl"
# Both classes "TextBox" and "DropDownList" implement the draw method

# class TextBox(UIControl):
#     def draw(self):
#         print("TextBox")


# class DropDownList(UIControl):
#     def draw(self):
#         print("DropDownList")
        
# Below we also have a function called "draw"
# that takes a UI Control Object called "control" and calls the "draw" method on it


# def draw(control):
#     control.draw()
    

# So with this we can create a "DropDownList" object called "ddl"

# ddl = DropDownList()

# and pass it to the "draw" function

# draw(ddl)

# Run the program

# This should work fine because the "ddl" object is an instance of the "UIControl" class
# To verify this, let's call "isinstance(ddl, UIControl)" and print the result to the terminal

# print(isinstance(ddl, UIControl))
# print(isinstance(ddl, DropDownList))

# So this means that the "DropDownList" object "ddl" is an instance of the class "UIControl"
# That implies that wherever we expect a "UIControl" object like "ddl"
# we can pass any of it's derivatives like "TextBox" or "DropDownList"

# *****************************
# Now what if we pass "TextBoox"

# textbox = TextBox()
# draw(textbox)

# **** Questions
# You might ask, what is the point of this?

# *** Let's take this to the next level
# We change the "draw" function "def draw(control)"
# Instead of getting a "control" object, i want it to get a LIST or a TUPLE of controls
# So we rename "control" to "controls" and ten we use a FOR LOOP to iterate over the "controls" object
# We pass a list of two objects "ddl" and "textbox" to the "draw" object when we call it

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass
    
class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")
        
# For "control" in "controls" we call the "draw" method on each control object

def draw(controls):
    for control in controls:
        control.draw()
        
ddl = DropDownList()
textbox = TextBox()

# We pass a list of two objects "ddl" and "textbox" to the "draw" object when we call it
draw([ddl, textbox])

# When we run the program
# We get two messages "DropDownList" and "TextBox" printed to the terminal

# So using this approach, you can render the user interface of an application
# Imagine you have a form with a bunch of text boxes, drop down lists, radio buttons and so on...

# You could have a list of all these objects and pass that list to a function like "draw"
# and that function will take care of rendering the entire form

# What is intersting here is that our draw function doesn't know what kind of control it's working with
# this is determined at runtime, it simply iterates over the list of controls and calls the "draw" method of each control object

# This is what we call "POLYMORPHISM"
# POLY = MANY
# MORPH = FORMS

# So POLYMORPHISM = MANY FORMS

# *********************
# In our example, our "draw" method is taking many different forms and this is determined at runtime
# We could be calling the "draw" method on a text-box or drop-down-list or radio button.