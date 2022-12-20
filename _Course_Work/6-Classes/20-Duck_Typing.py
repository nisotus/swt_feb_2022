# What we saw in the last session was a classic exmple of POLYMORPHISM

# To achieve POLYMORPHIC behaviour:

# You start by defining a base class like "UIContol" below
# In the base class "UIContol" we define the common behavior
# Or the common method that we need in the "UIContol" class derivatives or children


# With this, we achieve POLYMORPHIC behaviour in our "draw" function

# def draw(controls):
#     for control in controls:
#         control.draw()

# So depending on the type of control object you are working with at run time
# The "draw" method takes a different format

# It might be the "draw" method in a text-box, a drop-down-list or radio button and so on...

# This is how POLYMORPHISM works in all languages that support CLASSES

from abc import ABC, abstractmethod


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


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()


#******************

# But because Python is a dynamically typed language
# You don't necessarily need the "UIControl" as the base class

# So if we get rid of the "UIControl" base class
# We can still achieve POLYMORPHIC behaviour

class TextBox():
    def draw(self):
        print("TextBox")


class DropDownList():
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()



a = 5
b =  "Vini"

c = a * b

print(c)