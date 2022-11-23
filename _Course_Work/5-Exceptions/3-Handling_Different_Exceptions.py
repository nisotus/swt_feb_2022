# Division by zero exception

# try:
#     age = int(input("Enter your age: "))
#     gender = input("Enter your gender: ")
#     xfactor = 10 / age
#     gender_war = 10 / gender
#     print(xfactor)
#     print(gender_war)
# except ValueError:
#     print("Invalid age entered")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except TypeError:
#     print("Invalid gender entered")
# else:
#     print("No exceptions were thrown")

#*****************************

# When Python executes the code that we have in the "try" block
# If any of the statements throws an exception that matches one of the "except" clauses,
# that except clause is executed and the other except clauses are ignored

try:
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")
    xfactor = 10 / age
    gender_war = 10 / gender
    print(xfactor)
    print(gender_war)
except (ValueError, ZeroDivisionError, TypeError):
    print("Invalid input entered")
else:
    print("No exceptions were thrown")