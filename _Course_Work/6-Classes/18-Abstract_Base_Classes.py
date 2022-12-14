# We are going to continue with the example from the last session

# class Stream:
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InterruptedError("Stream is already opened.")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InterruptedError("Stream is already closed.")
#         self.opened = False


# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file")


# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a Network")

# There are a couple of issues with this implementation
# The first issue is that we can create a "Stream" object and call the "open()" method

# stream = Stream()
# stream.open()

# *** So what are the issues?

# *** The first issue
# The issue is because the "Stream" class is an abstract concept
# What does it mean to open a stream?

# Are we working with:
# A FILE STREAM
# A NETWORK STREAM

# *** The second issue
# If you look at the implementation of "FileStream" and "NetworkStream" classes
# You can see that both classes have a "read" method

# So currently in opur program, there is no way to enforce
# A common interface across different kinds of streams
# This is more of a convention we have used in our Program

# It will be nice to have a common contract or a common interface
# Across the different kinds of streams

# So how can we solve these two problems?
# The solution is to use an "ABSTRACT BASE CLASS"

# ****# So we want to make the "Stream" class an "Abstract Base Class"

# First we import the class "ABC" and method/function "abstractmethod" from "abc" module
# "abc" is the module
# "ABC" is the Abstract Base Class
# "abstractmethod" method will be used as a decorator

# *** Step 1
# from abc import ABC, abstractmethod

# *** Step 2
# To make the "Stream" class abstract, we should derive it from the "ABC" class

# *** Step 3
# We need to define a common interface for all streams
# We want all streams to have a read method and potentially a "write" method in the future
# So we define a "read" method with no implementation
# We decorate the "read" method with "abstract method decorator"

# With these 3 steps we have fixed both issues that we identified earlier

# from abc import ABC, abstractmethod

# class Stream(ABC):
#     def __init__(self):
#         self.opened = False
        
#     def open(self):
#         if self.opened:
#             raise InterruptedError("Stream is already opened.")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InterruptedError("Stream is already closed.")
#         self.opened = False
        
#     @abstractmethod
#     def read(self):
#         pass


# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file")


# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a Network")
        
# stream = Stream()
# stream.open()

# If we run the program, we get the error below:
# "TypeError: Can't instantiate abstract class Stream with abstract method read"

# Basically when a class has abstract method - in this case "Stream" class

# It is considered an abstract class and we cannot instantiate them
# Which means we cannot create an instance of them
# This is why we get the error - # "TypeError: Can't instantiate abstract class Stream with abstract method read"

# from abc import ABC, abstractmethod

# class Stream(ABC):
#     def __init__(self):
#         self.opened = False
        
#     def open(self):
#         if self.opened:
#             raise InterruptedError("Stream is already opened.")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InterruptedError("Stream is already closed.")
#         self.opened = False
        
#     @abstractmethod
#     def read(self):
#         pass


# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file")


# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a Network")
        
# class MemoryStream(Stream):
#     pass

        
# stream = MemoryStream()
# stream.open()

# stream = Stream()
# stream.open()

# So what is going on here?
# In our "Stream" class we defined an abstract method called "read"
# If a class derives from the "Stream" class, it has to implement the "read" method
# Otherwise the derived class will also be considered abstract

# Now in our example, our "MemoryStream" class is also abstract

# If we want to make the "MemoryStream" class a CONCRETE CLASS so we can intantiate it
# We will have to implement the "read" method for the "MemoryStream" class

from abc import ABC, abstractmethod

class Stream(ABC):
    def __init__(self):
        self.opened = False
        
    def open(self):
        if self.opened:
            raise InterruptedError("Stream is already opened.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InterruptedError("Stream is already closed.")
        self.opened = False
        
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a Network")
        
class MemoryStream(Stream):
    def read(self):
        print("Reading data from a Network")

        
stream = MemoryStream()
stream.open()