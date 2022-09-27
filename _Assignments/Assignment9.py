# SIMPLE CALCULATOR
# Write a Python program that can perform addition, subtraction, multiplication and division based on two inputs from the user
# The program should ask the user which of the four arithmetic operations below the user wants to perform:
# addition
# subtraction
# multiplication
# division

# Based on the selection of the operator by teh user, the selected arithmetic operator is performed and the result should be printed to the terminal.
while(1):
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number:  "))
    operation = input("""What do you want to do?
    -   for subtraction   
    +   for addition  
    /   for division  
    *   for multiplication    
    """)

    if (operation == '-'):
        print(f'Subtraction: {num1} - {num2} = {num1 - num2}')
    elif(operation == '+'):
        print(f'Addition: {num1} + {num2} = {num1 + num2}')
    elif(operation == '/'):
        print(f'Division: {num1} / {num2} = {num1 / num2}')
    elif(operation == '*'):
        print(f'Multiplication: {num1} * {num2} = {num1 * num2}')
    