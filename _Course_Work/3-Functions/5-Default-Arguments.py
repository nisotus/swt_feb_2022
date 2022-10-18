# def increment(number, by):
#     return number + by


# print(increment(number=2, by=1))

# ********Default Arguments
# def increment(number, by=1):
#     return number + by


# print(increment(number=2))

# ********************
# def increment(number=5, by=1):
#     return number + by


# print(increment(number=10, by=5))

# *****************************

# def increment(number=5, by=1):
#     return number + by


# print(increment())

# ***************************

def increment(number, another, mul=10, by=1):
    return number + by * mul - another


print(increment(2, 4, by=13))
