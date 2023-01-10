# In this session we learn about useful methods to work with files

from pathlib import Path
from time import ctime
import shutil

# path = Path("eCommerce/__init__.py")


# We can check to see if the file exists using the "exists()" method
# print(path.exists())

# We can rename it to "init.txt" using the "rename()" method
# path.rename("eCommerce/init.txt")

# We can delete the file by calling the "unlink()" method
# path.unlink()

# We can return information about the file using the "stat()" method
# path.stat()

# Let's see what the "stat()" method returns
# print(path.stat())

# import datetime
# mtime = path.stat().st_mtime
# atime = path.stat().st_mtime
# cctime = path.stat().st_ctime

# timestamp_str1 = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d-%H:%M')
# timestamp_str2 = datetime.datetime.fromtimestamp(atime).strftime('%Y-%m-%d-%H:%M')
# timestamp_str3 = datetime.datetime.fromtimestamp(cctime).strftime('%Y-%m-%d-%H:%M')
# print(timestamp_str1)
# print(timestamp_str2)
# print(timestamp_str3)

# We get a stacked result object with some attributes
# For example:
# st_size - returns the size of the file in bytes
# st_atime - returns the last access time
# st_mtime - returns the last modified time
# st_ctime - returns the creation time

# All the time values are in seconds after epic time
# Which is the start of time on a computer and it is platform dependent

# For example on Unix Systems, the epic time is January 1st 1970


# So to print the human readable time, we need to import the "ctime" function from the "time" module
# from time import ctime

# Now from the "stat()" object we can pick "st_ctime" = the creation time
# And pass it to the "ctime" function - "ctime(path.stat().st_ctime)"

# ctime(path.stat().st_ctime)
# print(ctime(path.stat().st_ctime))
# print(ctime(path.stat().st_mtime))
# print(ctime(path.stat().st_atime))

# *** Reading data from a file
# We also have a couple of methods for reading data from a file

# "read_bytes" returns the content of the file as a byte object for representing binary data
# path.read_bytes()
# print(path.read_bytes())

# *** Using the "read_text()" method
# "read_text" returns the content of the file as a string
# path.read_text()
# print(path.read_text())

# Using the ".read_text()" method is easier than the built-in "open()" function

# *** Using the "open()" function
# With the "open()" function we have to specify the filename for example "__init__.py"
# Then we need to specify the mode for example "rw"
# We also need to make sure we close the file using - file.close()

# file = open("__init__.py", "r")

# As a best practise we should use the "with" statement instead

# with file = open("__init__.py", "r") as file:
# ... then we can do something with the file

# *** Advantages of using "read_text()" method
# In contrast, when we use "read_text()" method, all the magic happens inside of the method
# So we no longer have to worry about opening, closing, mode etc..

# *** Using the "write_bytes()" method
# Similar to "read_text()" we also have the "write_text()" method
# path.write_bytes(data)

# *** Using the "write_text()" method
# Similar to "read_text()" we also have the "write_text()" method
# path.write_text("....")

# All these methods "read_bytes()", "read_text()", "write_bytes()", "write_text()"
# Take care of opening and closing the file, so we can do all kinds of operations with the file

# However, when it comes to copying a file, the "Path" object is not the ideal way to copy a file
# Let's have a look:

# Let's say we want to copy the "__init__.py" file to a different location
# We create source and target files in the respective directories
source = Path("eCommerce/__init__.py")
target = Path ("__init__.py")

# Then we use "read_text" method to read the file and pass it to "write_text" method
# target.write_text(source.read_text())

# Now the code above is a tedious way to do the copy
# We have a better way using a module called "shutil" or "Shell Utilities"
# The "shutil" provides a number of high level operations for copying and moving files and directories

# So on the top, import "shutil"
# Now with the "shutil" module, we can easily copy source to target using "shutil.copy(source, target)"
shutil.copy(source, target)

# This approach is cleaner and easier than using a "Path" object
