# Lets imagine that we want to create a function to save information about a user

# def save_user(**user):
#     return user


# user1 = save_user(id=100, name="Vincent", age=12)
# print(type(user1))

# *******************

def save_user(**user):
    print(user["age"])


save_user(id=100, name="Vincent", age=12)
