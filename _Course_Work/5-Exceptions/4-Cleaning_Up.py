# try:
#     file = open("1-Exceptions.py")
#     age = int(input("Enter Age: "))
#     divide_age = 20/age
#     file.close() # here is the problem
# except (ValueError, ZeroDivisionError):
#     print("You did not enter a valid age.")
# else:
#     print("No exceptions were thrown")

# try:
#     file = open("1-Exceptions.py")
#     age = int(input("Enter Age: "))
#     divide_age = 20/age
# except (ValueError, ZeroDivisionError):
#     print("You did not enter a valid age.")
#     file.close()
# else:
#     print("No exceptions were thrown")
#     file.close()

# *** Solution ***
# Use a "finally" clause at the end of the "else" clause

try:
    file = open("1-Exceptions.py")
    age = int(input("Enter Age: "))
    divide_age = 20/age

except (ValueError, ZeroDivisionError):
    print("You did not enter a valid age.")

else:
    print("No exceptions were thrown")

finally:
    file.close()

# The "finally" clause is always executed whether we have an excption or not
# We use the "finally" clause to release external resources

# *** So the "finally" clause is the best place to:
# Close Files
# Database Connections
# Network Connections
# and so on ...
