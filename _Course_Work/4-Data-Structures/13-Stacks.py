# In programming we have a common data structure called STACK
# which resembles a STACK of items in the real world

# *** LIFO: Last In - First Out
# Imagine you have a stack of books
# The last book that you put on top of the stack
# Is the first book that you can remove

# This is a stack data structure and it is very common in real world applications

# *** Browser Example
# A good example is your browser
# Whenever you navigate to a new website
# Your browser keeps your browsing sessions in a stack
# So when you click the back button, it takes you to the previous website

# *** How does this work
# It starts with an emptry stack
[]

# Let's say we navigate to website number [1]
[1]

# For simplicity we are using a number, if you are building a browser
# Instead of [1], we will use a string which is the address of the current website

# Now, let's say we navigate to a couple of websites
[1, 2, 3, 4, 5]

# and then click the "back" button
# at this point the broswer removes the item on top of the stack
# and then it will reditect us to the previous website
[1, 2, 3, 4]

# Now, let's say we press the "back" button a couple more times
# then we end up with an empty stack
[]

# At this point the browser will disable the "back" button
# This is how a stack works - Last In First Out

# *** How to use a STACK in Python
# Basically we can use a list object as a stack

# So we start with an empty list

# browsing_session = []

# Now let's say the user navigates to website number 1
# Then we call the append() method on browsing_session
# and add the address of the current website

# browsing_session.append(1)

# Now let's say the user navigates to website number 2
# Then we call the append() method on browsing_session
# and add the address of the current website

# browsing_session.append(2)

# Now let's say the user navigates to website number 3
# Then we call the append() method on browsing_session
# and add the address of the current website

# browsing_session.append(3)

# Now if we comine the code so far, we will get below:

# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)

# Now let's take a look at what we have in our stack

# print(browsing_session)

# Now, when the user presses the "back" button
# We should remove the last item in the list

# How do we do this?

# We use the pop() method

# So we have:
# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# print(browsing_session)

# This will remove the last item from the stack return it
# So let's store it in a variable called "last"
# But in this case, we are not going to use the value stored in variable "last"

# last = browsing_session.pop()
# print(last)

# Now, let's print the browsing session

# print(browsing_session)

# So we need to take the user to previous website
# which is the item on top of the current stack
# How do we do that?

# We can achive that by using a negative 1 (-1) index

# browsing_session[-1]

# We print it

# print(browsing_session[-1])

# We can also add a label for clarity

# print("redirect", browsing_session[-1])

# When the user presses the "back" button
# we redirect them to the previous website, which is website number 2

# Now we need to check if the stack is empty or not
# If it becomes empty, we need to disable the "back" button

# How do we do this?

# Earlier in the course we discussed about the "Falsy" values
# 0 - Zero is a Falsy Value
# "" - Empty string is a Falsy Value
# [] - Empty list is a Falsy Value

# If we apply the "not" operator to a "Falsy" Value, then we get teh Boolean "True"

# So to see if our stack is empty, we can simply write code like this

# if not browsing_session:
#     print("disable")
    
# Our code soe far will look like below:
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session[-1])
if not browsing_session:
    print("disable")

print(browsing_session)
    
# So the final program will look like below:

# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# if not browsing_session:
#     browsing_session[-1]
    
# print(browsing_session)
