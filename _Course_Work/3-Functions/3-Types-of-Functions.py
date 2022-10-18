# TWO TYPES OF FUNCTIONS

# Type-1: Function that performs a task
# Type-2: Function that returns a value

# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome Aboard")


# greet("Dunni", "Adesoba")


# def greeting(name):
#     print(f"Hi {name}")


# # greeting("Ade")


# message = greeting("Ade")
# print(message)


# # **** Writing to a file

def greeting(name):
    return f"Hi {name}"


message = greeting("Ade")


my_file = open("dunni.pdf", "w")

my_file.write(message)

# print(greeting("Olu"))
