# In almost every program, there are times you need to make a DECISION and that is when you use an IF STATEMENT

# Below is an example

temperature = 35
if temperature > 30:
     print("It is warm")
     print("Drink some water")

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

temperature = 15
if temperature > 30:
    print("It is warm")
    print("Drink some water")
elif temperature > 20:
    print("It's nice weather")
else:
    print("its Cold")

print("Done")


# Grades from 0 to 100
# A - 75 to 100
# B - 65 to less than 75
# C - 50 to 64
# D - 40 to 49
# F - Below 40

# score = int(input("Enter Student Score: "))
# score = float(input("Enter Student Score: "))

# if score < 40:
#     print("Student Grade is F")
# if score >= 40 and score < 50:
#     print("Student Grade is D")
# if score >= 50 and score < 65:
#     print("Student Grade is C")
# if score >= 65 and score < 75:
#     print("Student Grade is B")
# if score >= 75 and score <= 100:
#     print("Student Grade is A")


# Using "elifs"

#score = float(input("Enter Student Score: "))

#if score < 40:
 #   print("Student Grade is F")
#elif score >= 40 and score < 50:
   # print("Student Grade is D")
#elif score >= 50 and score < 65:
 #   print("Student Grade is C")
#elif score >= 65 and score < 75:
 #   print("Student Grade is B")
#elif score >= 75 and score <= 100:
 #   print("Student Grade is A")
