from random import random
from unicodedata import name



#some examples of functions (mini program that complete a specific task)
# print("hello World")

# name = input("Enter your name: \n")

# amount = int(1,6)

# roll = random.randit(1,6)


#defining a functions, the functions needs to be defined first, before they are called. 
#A variable created inside a function can only be used inside that function(i.e  called a local scope)
# A variable created in the main program of a is a global variable and has a global scope. That means it can be used anywhere.
#NOTE: you follow this format whenever you are defining a function: def   function name   (parameter):

# def greeting(name):                                                 #3rd step execution by the computer
#     print("hello", name)                      #the functions need to be defined first
    
# #main program
# input_name = input("Enter your name:\n")        #The computer start to execute from the main program(1 step)

# greeting(input_name)                           #before they are called in the main program, just like you need to define a variable before you can use it.
                                                # (2nd step execution by computer)
                                                
                                            
                                            
#2nd example by creating a variable in the main body of the program(global variable), which can be used anywhere.

# def greetings():
#     print("Hello", name)
    
# #main program                                   #the variable name is global.
# name = input("Enter your name : \n")            
# greetings()                                        #we dont need a parameter for the greeting() since it can reference the global variable name.
                                                    #the grretings function will be callled
                                                
                                                


# #3rd example. Use a global variable and enter 2 names

# def greeting():
#     print("hello", name)
# #main program
# name1 = input("enter your name: \n")
# greeting()
# name2 = input("enter another name: \n")
# name = name2
# greeting()


# #local scope allow us to re-use the greetings function with different values

# def greeting(name):
#     print("hello", name)
    
# #main program
# name1 = input("Enter your name: \n")
# greeting(name1)
# name2 = input("Enter another name: \n")
# greeting(name2)

##We create a function so as to reuse that chunk of code over and over. example the greeting function was reused for two different names.



#Example: We want a simple function that adds two numbers and returns the result.

def addition (a,b):                                             #step 4
    return(a + b)                                               #step 5

#mainprogram
num1 = float(input("Enter your 1st number: \n"))                #computer execution step 1
num2 = float(input("Enter your 2nd number: \n"))                 #step2
#calling our addition function that has been defined above:         
result = addition(num1, num2)                                      #step 3
print("The result is", result)                                      #step 6


