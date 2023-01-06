# When we run the "app.py" program, you will see a new folder called "__pycache__"
# In the "__pycache__" folder we have a compiled version of the modules that we import into our program

# *** Question
# How does Python know if the compiled version is up-to-date with the latest code in the compiled module?
# It basically checks the date-time of the two files "sales" and "sales.cpython-39.pyc"

# The "cpython-39.pyc" that you see in the name represents the Python implementation used for compilation
# In the "sales.cpython-39.pyc" file, we have Python byte-code
# When we click the file, VS Code does not show the content by default because it is binary
# But if you click the link in the file, we can see the Python byte-code representation

# Note that we don't have the compiled version of the "app" module
# This is because Python always recompiles the module that we load directly from the command line

# So in this demo, we passed "app.py" as the entry point
# That's the reason Python did not cache the compiled version of "app.py"