# Below we have a "path" object that represents a directory

from pathlib import Path

# path = Path("c://Programming//Python_SWT//swt_feb_2022//_Course_Work//8-Python_Standard_Library//Vincent")
path = Path("Vincent")

# A few useful methods that you need to be aware of are:

# print(path.exists())  # Returns a boolean
# path.mkdir()  # To create the directory specified in *Path("ecommerce")*
# path.rmdir()  # To remove the directory
# path.rename("c://Programming//Python_SWT//swt_feb_2022//_Course_Work//8-Python_Standard_Library//Vincent30")  # To rename the directory to a new name
# path.rename("Vincent30")  # To rename the directory to a new name

# Now let us look at another method called "iterdir"

# With "iterdir" we can get a list of files and directories in object "path"
# So let's print the results

print(path.iterdir())

# We get a generator object - "<generator object Path.iterdir at 0x000002258AA99510>"
# A generator object as the name implies, returns a new value every time we iterate it
# So when we are working with a large list of items, instead of storing all those items in memory
# We use a generator object, we iterate it and get a new value everytime - this is more efficient

# When working with files and directories, it is possible to have a directory with a million files in it.

# So we can iterate over our object "path"

# for p in path.iterdir():
#     print(p)
    
# The result will be the names of the list of files and directories in the "path" object

# Now, if you are working with a directory that does not have ten of millions of files in it
# You can convert the generator to a list using a LIST COMPREHENSION EXPRESSION

# This is the SYNTAX for LIST COMPREHENSION - "[expression for item in items]"

# paths = [p for p in path.iterdir()]
# print(paths)

# paths = [print(p) for p in path.iterdir()]

# *** Note
# Notice that we get an array of "WindowsPath" objects for Windows OS and "PosixPath" objects for Mac OS
# So what is "WindowsPath" or "PosixPath"?

# The "Path" class that we imported on the top is the base class for two different classes
# PosixPath
# WindowsPath

# PosixPath is the standard used in Unix-Like OS
# WindowsPath is the standard used in Windows OS


# *** Next Level
# Now we can take the list comprehension expression to the next level and apply filtering
# Let's say we only want to get the directories

# paths = [p for p in path.iterdir() if p.is_dir()]
# print(paths)

# paths = [print(p) for p in path.iterdir() if p.is_dir()]

# *** Limitations
# So the method ".iterdir()" is pretty useful to get the list of files and directories in a path
# But it has two limitations

# *** Limitation 1
# We cannot search by a pattern

# *** Limitation 2
# It does not search recursively

# *** Remedy
# So to be able to search by a pattern or recursively we need to use a different method called "glob"

path.glob("*.*")  # To search for all files
# path.glob("*.py")  # To search for all ".py" files

# for files in path.glob("*.*"):
#     print(files)

# Similar to ".iterdir()", the "glob()" method also returns a generator
# So we can use it in a LIST COMPREHENSION
    
# This is the SYNTAX for LIST COMPREHENSION - "[expression for item in items]"

# all_files = [print(files) for files in path.glob("*.*")]
# all_py_files = [print(files) for files in path.glob("*.py")]
# all_txt_files = [print(files) for files in path.glob("*.txt")]

# To search recursively, we need to change the pattern "*.py" to "**/*.py"

# py_files = [p for p in path.glob("**/*.py")]
# print(py_files)

# all_files_recursively = [print(files) for files in path.glob("**/*.*")]

# The other option to search recursively is to use the "rglob()" method
# "rglob()" is the short for RECURSIVE-GLOB
# py_files = [p for p in path.rglob("*.py")]
# print(py_files)

all_files_recursively = [print(files) for files in path.rglob("**/*.*")]