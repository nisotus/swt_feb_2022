# Now let's look at a good exmaple of INHERITANCE
# Let's imagine we want to model the concept of a stream of data

# *****************************
# We can read a stream of data from:
# A FILE
# A NETWORK
# THE MEMORY

# *****************************
# All these streams have a few things in common, we can:
# OPEN THEM
# CLOSE THEM
# READ DATA FROM THEM

# *****************************
# But how we read data from a stream is dependent upon the type of stream
# Because reading data from a file is different from reading it from a network

# *****************************
# Here we are creating a custom exception class
# By convention, all custom exceptions should end with the word "Error"
# Note that we are deriving "InvalidOperationError" from the base "Exception" class in Python
# So every time you want to create a custom exception you should derive your class from the "Ecxeption" class

class InvalidOperationError(Exception):
    pass

# we start by defining a base class called "Stream"

class Stream:
    # Let's say we need a flag to know if the stream is open or not
    def __init__(self):
        self.opened = False
    
    # then we define method "open"
    def open(self):
        # What if we try to open a stream that is already opened?
        # That is an invalid operation, so we want to raise a custome exception called "InvalidOperationError"
        # We need to create a class for the "InvalidOperationError" since we donät have this in Python 
        if self.opened:
            raise InvalidOperationError("Stream is alredy opened.")
        self.opened = True
    
    # Then we define method "close"
    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False
        
# *****************************
# So the program above captures the common features that we need in every stream

class InvalidOperationError(Exception):
    pass

class Stream:
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

# *****************************
# Now let's go ahead and implement "FileStream" and "NetworkStream" classes
# Remember that how we read data from a file is different from how we read data from a newtork

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")
        
        
class NetworkStream(Stream):
    def read(self):
        print("Reading data from a Network")
    
# Now this is a good example for inheritance