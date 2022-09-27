# SIMPLE CALCULATOR USING TENARY OPERATOR
# Write a Python program that can perform addition, subtraction, multiplication and division based on two inputs from the user
# The program should ask the user which of the four arithmetic operations below the user wants to perform:
# addition
# subtraction
# multiplication
# division

# Based on the selection of the operator by teh user, the selected arithmetic operator is performed and the result should be printed to the terminal.

num1 = int(input("Enter first number:   "))
num2 = int(input("Enter second number:  "))
opr = input("""What do you want to do?
    -   for subtraction   
    +   for addition  
    /   for division  
    *   for multiplication    
    """)

(print(f'Subtraction: {num1} - {num2} = {num1 - num2}') if opr == '-' else 
print(f'Addition: {num1} + {num2} = {num1 + num2}') if opr == '+' else
print(f'Division: {num1} / {num2} = {num1 / num2}') if opr == '/' else
print(f'Multiplication: {num1} * {num2} = {num1 * num2}'))