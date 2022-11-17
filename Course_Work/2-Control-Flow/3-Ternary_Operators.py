# # In this session we will look at a technique for writing cleaner code

# # Let's say you are building an application for a university and you want to check to see if the person who is applying for a university programme
# # Is eligible or not based on their age

# # age = int(input("Enter student age: "))
# # if age >= 18:
# #     print("Eligible")
# # else:
# #     print("Not Eligible")

# # There is nothing wrong in the code above, but we have a cleaner way to write this

# # age = int(input("Enter student age: "))
# # if age >= 18:
# #     message = "Eligible"
# # else:
# #     message = "Not Eligible"

# # print(message)

# # Now when we have an IF ELSE statement with the structure above where you are basically assigning a value to a variable
# # You can re-write this in a simpler way

# age = int(input("Enter student age: "))
# # What we have here is called "Ternary Operator"
# message = "Eligible" if age >= 18 else "Not Eligible"
# print(message)

# # (True Path) (Condition) (False Path)
# # Any additional statements

age = int(input("Enter the student age: \n"))

if age > 18:
    print("Eligible")
else:
    print("Not Eligible")