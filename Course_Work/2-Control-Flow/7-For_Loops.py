# For simplicity, let us create a print message to send
# print("Sending a message")

# Now if we want to re-send this message three times, we can do it like below:
# print("Sending a message")
# print("Sending a message")
# print("Sending a message")

# This is ugly

# This is where you want to use a LOOP. We use LOOPS to create repitition.

# How does LOOP work

# The FOR statement

# for i in range(10):
#     print("Sending Message")

# for number in range(3):
#     print("Sending Message")


# for number in range(3):
#     print("Attempt", number)

# We get 0 1 2
# Attempt 0
# Attempt 1
# Attempt 2

# The FOR LOOP is executed 3 times, in each iteration, "number" will have a different value
# The 1st iteration it will be "0"
# The 2nd iteration it will be "1"
# The 3rd and final iteration it will be "2"

# for number in range(3):
#     print("Attempt", number + 1)



# for number in range(3):
#     print("Attempt", number + 1, number + 1)

# for number in range(3):
#     print("Attempt", number + 1, (number + 1) * "." )


# for number in range(1, 4):
#     print("Attempt", number)

# for number in range(1, 10, 2):
#     print("Attempt", number)

for number in range(1, 10, 2):
    print("Attempt", number, (number) * ".")