# SIMPLE CALCULATOR
# Write a Python program that can perform addition, subtraction, multiplication and division based on two inputs from the user
# The program should ask the user which of the four arithmetic operations below the user wants to perform:
# addition
# subtraction
# multiplication
# division

# Based on user selection, the selected arithmetic operator is performed and the result should be printed to the terminal.


print("What operation do you want? ")
operator = input("Enter either +, -, * or /: ")

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

# if operator == "+":
#     print(n1, operator, n2, "=", n1 + n2)

# elif operator == "-":
#     print(n1, operator, n2, "=", n1 - n2)

# elif operator == "*":
#     print(n1, operator, n2, "=", n1 * n2)

# elif operator == "/":
#     print(n1, operator, n2, "=", n1 / n2)

# else:
#     print("Invalid Operator")

(print(n1, operator, n2, "=", n1 + n2) if operator == "+" else 
print(n1, operator, n2, "=", n1 - n2) if operator == "-" else 
print(n1, operator, n2, "=", n1 * n2) if operator == "*" else 
print(n1, operator, n2, "=", n1 / n2) if operator == "/" else 
print("Invalid Operator"))