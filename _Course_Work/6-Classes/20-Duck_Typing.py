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


# *** How is this possible
# Here is the reason:
# So Python does not care if these objects derive from the "UIControl" class
# As long as these objects have a "draw" method, Python will be happy
# So technically we can pass a STRING, LIST, TUPLE, DICTIONARY - Anything ITERABLE

# In thesame token, that iterable object, it's individual parts should have a "draw" method



# *** To Recap
# To achieve POLYMORPHISM we don't necessarily need a base class like "UIControl"
# because Python supports DUCK TYPING

# However, having the "UIControl" as an abstract base class is a good practice
# because it enforces a common interface or a common contract across all it's derivatives
# With this we can make sure that every kind of "UIControl" will have a "draw" method