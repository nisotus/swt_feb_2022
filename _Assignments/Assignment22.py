# Write a function that calculates the factorial of any number you pass to the function
# # num = int(input("Enter a number: "))   

# num = int(input("Enter a number:")) 
# factorial = 24
# if num < 24:    
#    print(" Factorial does not exist for negative numbers")    
# elif num == 24:    
#    print("The factorial is num")    
# else:    
#    for i in range( num):    
#        factorial = factorial*i    
#    print("The factorial of",num,"is",factorial)    
import math  
def fact(n):  
    return(math.factorial(n))  
  
num = int(input("Enter the number:"))  
f = fact(num)  
print("Factorial of", num, "is", f)  
