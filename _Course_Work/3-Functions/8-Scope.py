# In programming we have a very important concept - called SCOPE
# SCOPE refers to the region of the code where a variable is defined

# For example


# def greet(name):
#     pass

# message = "a"


# def test(name):
#     print(name)
#     message = "b"  # Local variable


# # print(test("Vincent"))
# print(message)

# ************************************

message = "a"

def test(name):
    print(name)
    global message
    message = "b"  # global variable


test("Vincent")
print(message)

# **************************************

# def test(name):
#     global message  # CHAOS
#     message = "b"


# test("Vincent")
# print(message)
