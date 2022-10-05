# SIMPLE CALCULATOR USING TENARY OPERATOR
# Write a Python program that can perform addition, subtraction, multiplication and division based on two inputs from the user
# The program should ask the user which of the four arithmetic operations below the user wants to perform:
# addition
# subtraction
# multiplication
# division

# Based on the selection of the operator by teh user, the selected arithmetic operator is performed and the result should be printed to the terminal.



num1= int(input("Enter the first number: \n"))
num2 =int( input("Enter the second number: \n"))

operat = input("""Which of the four arithmetric operations do you want to perform?
                 - for subtraction
                 + for addition
                 * for multiplication
                 """)


    
subtraction = num1 - num2
print(subtraction)
addition = num1 + num2 
print(addition)
multiplication = num1 * num2
print(multiplication)


if operat == "-":
    print(subtraction = {num1} - {num2})
    
elif operat == "+":
    print(addition = {num1} + {num2})
    
else:
    print(multiplication = {num1} * {num2})