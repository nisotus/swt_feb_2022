# In this session we will see how to find and fix bugs in your program
# Below is the multiple function we wrote earlier

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print(multiply(1, 2, 3, 4, 5, 6))

# *************************

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("Start")
print(multiply(1, 2, 3, 4, 5, 6))
print("End")
