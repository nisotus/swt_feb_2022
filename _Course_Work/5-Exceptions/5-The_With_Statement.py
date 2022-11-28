# In the last session we learnt that we use the "finally" clause to release external resources
# We have a shorter and cleaner way to achieve the same result without the "finally" clause

# *** Note that it does not always work, it works with certain kinds of objects

# try:
#     file = open("exceptions.txt")
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You did not enter a valid age.")

# else:
#     print("No exceptions were thrown")

# finally:
#     file.close()
    
# See how it work with the shorter and cleaner way of doing this...
# *** We use the "with" statement

# Whenever we open a file using the "with" statement
# Python will automatically call "file.close()", whether we have a final clause or not

# try:
#     with open("exceptions.txt") as file:
#         print("File Opened.")
#         age = int(input("Age: "))
#         xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You did not enter a valid age.")

# else:
#     print("No exceptions were thrown")

# finally:
#     file.close()
    
# In other words, the "with" is used to automatically release external resources
# So we can remove the "finally" clause from our code

try:
    with open("exceptions.txt") as file:
        print("File Opened.")
        age = int(input("Age: "))
        xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You did not enter a valid age.")

else:
    print("No exceptions were thrown")


# *** How does this work under the hood. Let's dive deeper

file.__enter__ 
file.__exit__

# *** Now to take this to the next level
# How do you handle multiple external resources
# Let's say you want to read something from one file and write it to another file

# In the "with" statement, you can add a comma "," and open another external resource

# *** How does this work under the hood. Let's dive deeper
# If we look at the file object by typing "file."
# We will see methods that start and end with double underscore- for example "__start__"
# We refer to these methods as "MAGIC METHODS"

# We will learn more about MAGIC METHODS when we talk about CLASSES

# With the "file" object, we have two magic methods that you should be aware of:

# *** "__enter__" and "__exit__"

# When our object has these two methods, we say the object supports "CONTEXT MANAGEMENT PROTOCOL"
# We will also talk about "CONTEXT MANAGEMENT PROTOCOL" in the next sessions

# So if an object supports - "CONTEXT MANAGEMENT PROTOCOL"
# Or in other word, if an object has the two methods - "__enter__" and "__exit__"
# We can use that object with the "with" statement

# Python will automatically call the "__exit__" method and it will release external resources
# That is why we don't need the "finally" clause

try:
    with open("exceptions.txt") as file, open("another.txt") as target:
        print("File Opened.")
        age = int(input("Age: "))
        xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You did not enter a valid age.")

else:
    print("No exceptions were thrown")