# Over the next few session, we will learn how to work with files and diretories in Python
# In this session we are going to look at the "Path" class
# Because the "Path" class is the foundation to working with files and directories

# So the first thing to do is import the class "Path" from the "pathlib" module


from pathlib import Path

# Now we can create a "Path" object in a few different ways

# *** Absolute Path
# We can create an absolute path, for example if you are on WINDOWS
# You can create a "Path" object like below:

#*** WINDOWS
Path("C:\\Program Files\\Microsoft")

# When working with a long path, the backlashes "\\" can get a little ugly
# We can simplify this by using a raw string.
# In a raw string, backslash is not an escape character, it's taken literally as is

# To have a RAW STRING, we prefix the string with an "r" and get rid of the second backlash

Path(r"C:\Program Files\Microsoft")

#*** MAC or LINUX

Path("/usr/local/bin")

#*** Current Folder
# We can also create a Path object that represents the current folder

Path()

# *** Relative Path
# Or we can use a relative path

Path("eCommerce/__init__.py")

# *** Combine Path Objects together
# We can also combine path objects together

Path() / Path("eCommerce")

# We can also combine a "Path" object with more than one STRING

Path() / "eCommerce" / "__init__.py"

# We can get the HOME DIRECTORY of the current user
Path.home()

# So above are several ways to create a "Path" object,
# but for this demo we will use - Path("ecommerce/__init__.py")

# So we have:

path = Path("_Course_Work\\8-Python_Standard_Library\\eCommerce\\__init__.py")

# So the "path" object has a few useful members, but we will look at the most important ones
# If you want to see the comprehensive list, go to - https://docs.python.org/3/library/pathlib.html
# So with the "path" object we can do below:

path.exists() # To see if the file or directory exists
path.is_file()  # To check if the path represents a file
path.is_dir()  # To check if the path represents a directory


print(path.exists())
print(path.is_file())
print(path.is_dir())

# We can also extract individual components in the path, which is extremely useful
# For example, let's print path.name

print(path.name) # It will return only the file name in the path with extension

# We also have:
print(path.stem)  # returns the filename without the extension

# If you want to get the extension, you can access the "suffix" attribute
print(path.suffix)

# We can also get the parent of the path
print(path.parent)  # this returns the parent folder

path = path.with_name("vince.txt")
print(path)

# We can also get the absolute value of the path
# Obviously the "vince.txt" file does not exist yet, we are only representing it's path
print(path.absolute())

# C:\Programming\Python_SWT\swt_feb_2022\_Course_Work\8-Python_Standard_Library
# C:\Programming\Python_SWT\swt_feb_2022\_Course_Work\8-Python_Standard_Library\eCommerce

path = path.with_suffix(".doc")
print(path)

# Note that in any of these cases, we have not renamed the path
# we are only representing a path object

# So these are the important members of the "Path" class that we should note

# Over the next sessions we will see how to rename files and directories