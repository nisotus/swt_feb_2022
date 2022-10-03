# Write a Python program for a car wash system
# The car wash has 4 levels of washing (Normal, Basic, Gold, Platinum)
# The cost is calculated based on the level and the car size (Small, Medium, Large)

# I want you to think of an approach to to implement this solution by using prices (for the different levels) and numbers for the car size.
# You will need to multiply these values to get a washing cost
# You need to take all the values that is needed as input and display the final cost based on the input from the customer

# Name
# Level
# size
# payment amount

washLevels = 25, 35, 50, 70
carSizes = 5, 7, 10
level, size = 0, 0

name = input("Enter name here:  ")
while level == 0:
    data = input("""
    1 for Normal
    2 for Basic
    3 for Gold
    4 for Platinum
    Enter number for wash level:    """)
    if not (data.isdigit() and (0 < int(data) < len(washLevels) + 1)):
        print("Invalid level selected. Please try again ")
    else:
        level = int(data)

while size == 0:
    data = input("""
    1 for Small
    2 for Medium
    3 for Large
    Enter number for car size:  """)
    if not (data.isdigit() and (0 < int(data) < len(carSizes) + 1)):
        print("Invalid level selected. Please try again ")
    else:
        size = int(data)

print(f'\n\nHello {name}')
print(f'The cost for your wash is {washLevels[level -1] * carSizes[size -1]}kr')
