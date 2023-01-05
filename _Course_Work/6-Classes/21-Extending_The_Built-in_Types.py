#  For example, we can create a class "Text" and have it inherit from the built-in string class "str"

# With this our "Text" class will inherit all the features of Python STRINGS
# but we can also add additional features to it

class Text(str):
    def duplicate(self):
        return self + self
    
# "self" represents the current object which is an instance of a string class
# With "self + self" we are concatenating a string with itself

text = Text("Nigeria")

# if we type "text." we will see that our "text" object has all the methods of Python STRINGS
# So we can convert it to lower case and print it

print(text.lower())
print(text.upper())

# Pretty useful right!!!!

# ********Another example
# We can also extend Python LISTS
# So let's define a new class, call it "TrackableList" that inherits from the built-in LIST class "list"
# Define a method called "append" to override the default "list append method"

# So everytime we want to append an object to the list,
# we want to print a message on the terminal, perharps for logging
# we will also need to call the "append" method of the super or base class = "list" class
# So we call - "super().append()" and pass "object" to "append()" = "super().append(object)"

class TrackableList(list):
    def append(self, object):
        print("Append Called")
        super().append(object)


# So technically we are extending the "append" method of the list class, we are not replacing it

# Now we can create a list object using the class "TrackableList"

list = TrackableList()

# if we type "list." we will see that our "list" object has all the methods of Python LISTS

list.append("1")

# When we run the program we can see the message "Append called" in the terminal

# As you can see, extending built-in types in Python is very easy