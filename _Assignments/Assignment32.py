# Write a function for checking the speed of drivers. This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”.

# If the driver gets more than 12 points, the function should print: “License suspended”


def checkSpeed(speed):
    speed_limit = 70
    if (speed <= speed_limit):
        print ("OK")

    if (speed > speed_limit):
        over_limit = speed - speed_limit
        dpoint = over_limit // 5
        if dpoint <= 12:
            print(f"Demerit point is: ", dpoint)
        elif dpoint >= 13:
            print("License suspended")
            print("Your License is now suspended since you are", over_limit, "km above speed limit")


checkSpeed(int(input("Enter speed: ")))

