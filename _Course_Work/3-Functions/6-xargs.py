# def multiply(x, y):
#     return x * y


# print(multiply(2, 5))

# print(multiply(2, 5, 7, 9))

# ***********Using xargs
def multiply(*numbers):
    start = 1
    for num in numbers:
        start = num * start
    return start


print(multiply(2, 1, 3, 3, 6, 7, 8, 10))


# ***************************
# def multiply(*names):
#     return names


# print(multiply(2, 1, 3, 4))
