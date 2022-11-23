# In almost every program, there are times you need to make a DECISION and that is when you use an IF STATEMENT

# Below is an example

# temperature = 35
# if temperature > 30:
#     print("It is warm")
#     print("Drink some water")

# # This will be executed where our condition "if temperature > 30" is True or False
# print("Done")

# Be careful about the indentation, because it is very important in Python

# What if we have multiple conditions, we use an "elif" statement
# temperature = 15
# if temperature > 30:
#     print("It is warm")
#     print("Drink some water")
# elif temperature > 20:
#     print("It's nice weather")

# print("Done")

# You can also have "else" statement to be execute if none of the "ifs" and "elifs" are True

# temperature = 15
# if temperature > 30:
#     print("It is warm")
#     print("Drink some water")
# elif temperature > 20:
#     print("It's nice weather")
# else:
#     print("its Cold")

# print("Done")


#Grades from 0 to 100
# A - 75 to 100
# B - 65 to less than 75
# C - 50 to 64
# D - 40 to 49
# F - Below 40

score = int(input("Enter Student Score: "))
score = float(input("Enter Student Score: "))

if score < 40:
    print("Student Grade is F")
if score >= 40 and score < 50:
    print("Student Grade is D")
if score >= 50 and score < 65:
    print("Student Grade is C")
if score >= 65 and score < 75:
    print("Student Grade is B")
if score >= 75 and score <= 100:
    print("Student Grade is A")


# Using "elifs"


#score = float(input("Enter Student Score: "))

# if score < 40:
#   print("Student Grade is F")
# elif score >= 40 and score < 50:
# print("Student Grade is D")
# elif score >= 50 and score < 65:
#   print("Student Grade is C")
# elif score >= 65 and score < 75:
#   print("Student Grade is B")
# elif score >= 75 and score <= 100:
#   print("Student Grade is A")

# try:
#     score = float(input("Enter Student Score: "))
#     if score >= 0 and score < 40:
#         print("Student Grade is F")
#     elif score >= 40 and score < 50:
#         print("Student Grade is D")
#     elif score >= 50 and score < 65:
#         print("Student Grade is C")
#     elif score >= 65 and score < 75:
#         print("Student Grade is B")
#     elif score >= 75 and score <= 100:
#         print("Student Grade is A")
#     else:
#         print("Invalid Score")
# except ValueError:
#     print("Invalid Score")

# ************************************************************

# score = float(input("Enter Student Score: "))
# if score >= 0 and score < 40:
#     print("Student Grade is F")
# elif score >= 40 and score < 50:
#     print("Student Grade is D")
# elif score >= 50 and score < 65:
#     print("Student Grade is C")
# elif score >= 65 and score < 75:
#     print("Student Grade is B")
# elif score >= 75 and score <= 100:
#     print("Student Grade is A")
# else:
#     print("Invalid Score")


# if - will secure a category or partition of input

# elif - each elif will also secure a different partition or category of input
# You can have several elifs

# else - will secure category of input that the if and elif cannot or did not secure


# score = input("Enter Student Score: ")

# if((score.isdigit())):

#     score = int(score)
#     if score >= 0 and score < 40:
#         print("Student Grade is F")
#     elif score >= 40 and score < 50:
#         print("Student Grade is D")
#     elif score >= 50 and score < 65:
#         print("Student Grade is C")
#     elif score >= 65 and score < 75:
#         print("Student Grade is B")
#     elif int(score) == score and score >= 75 and score <= 100:
#         print("Student Grade is A")

# else:
#     print("Invalid Score")
# >>>>>> > 898f8345bab33cb63081945f1a2206d21e849893
