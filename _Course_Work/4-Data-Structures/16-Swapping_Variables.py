# Let's look at something very cool

# We define two variable

x = 10
y = 11

# Can you write a program that will swap these two variables
# Meaning that I want to have 11 in x and 10 in y

# *** Solution

# To swap two varibles we need a third variable

x = 10
y = 11

# We define a third variable "z" and set it to "x"
# Basically we are copying the value of "x" into a separate variable "z" as a backup

z = x

# Now we can override "x" with "y"
# We copy the value of "y" to "x"

x = y

# Now we have the old value of "x" stored in "z"

# So we can use that to override "y"

y = z

# The code will look like below:

x = 10
y = 11

z = x
x = y
y = z

# With these three lines we can swap the value of these two variables
# So, let's print "x" and "y"

# print("x", x)
# print("y", y)

# We can see that x = 11 and y = 10

# *** Better Solution
# In Python, we can swap the values of two variables
# Using only one line of code and without the need for a third variable

x = 10
y = 11
z = 12

x, z, y = z, y, x

print("x", x)
print("y", y)
print("z", z)

# *** Explanation
# Looking at the code - "x, y = y, x"
# We are defining a TUPLE with the code on the right side of the assignment operator "y, x"
# It is the same as "x, y = (y, x)"
# So what we are doing is that we are UNPACKING a TUPLE

# So we define a TUPLE on the RIGHT SIDE and UNPACKING it on the LEFT SIDE

x, *y, z = [1,2,3,5,6,6]
print(x)
print(y)
print(z)
