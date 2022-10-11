# TWO TYPES OF FUNCTIONS

# Type-1: Function that performs a task
# Type-2: Function that returns a value

# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome Aboard")


# print()
# greet()


# def greeting(name):
#     print(f"Hi {name}")


# greeting("Ade")


# ***********************************


# message = greeting("Ade")
# print(message)


# # **** Writing to a file
from pyparsing import oneOf


def greeting(name):
    return f"Hi {name}"


# message = greeting("Ade")


# jagaban = open("vincent.txt", "w")

# jagaban.write(message)

# print(greeting("Olu"))
