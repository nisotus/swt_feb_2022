# age = int(input("Age: "))

# To handle the exception in this program, we need to put the code
# that triger the exception in a TRY block

# try:
#     age = int(input("Age: "))
# except ValueError:
#     print("You did not enter a valid age")
    
# When Python sees a TRY block. It will execute every statement in the TRY block
# If any of the statements in the "try" block throws an exception
# The code in the "except" clause will be executed

# try:
#     age = int(input("Age: "))
#     sex = input("Enter your gender: ")
#     birth_year = int(input("Enter your birth year: "))
#     height = float(input("Enter your height: "))
# except ValueError:
#     print("You did not enter a valid age")
    
# If you don't have any exceptions, the code in the "except" clause will not be executed

# ************Using "else" with "try" and "except"
# You can also add an "else" block after the "try" and "except" block

# try:
#     age = int(input("Age: "))
#     sex = input("Enter your gender: ")
#     birth_year = int(input("Enter your birth year: "))
#     height = float(input("Enter your height: "))
# except ValueError:
#     print("You did not enter a valid age")
# else:
#     print("No exceptions were thrown")
    
# print("Execution Continues")

# print("Execution Finished")



# *****

try:
    age = int(input("Age: "))
except ValueError as dunni:
    print("You did not enter a valid age")
    print(dunni)
    print(type(dunni))
else:
    print("No exceptions were thrown")
    
print("Execution Continues")

print("Execution Finished")
