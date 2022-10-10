# for x in range(5): # Outer Loop
#     for y in range(3): # Inner Loop
#         print(f"({x},{y})")

# for x in range(3): # Outer Loop
#     for y in range(5): # Inner Loop
#         print(f"({x},{y})")

for firstname in ["Joe", "Vincent", "Joysy", "Muyiwa", "Jessica"]:
    for lastname in ["Uche", "Oke", "Enoo", "Oni", "Aiziotogbe"]:
        # print(f"{firstname}, {lastname}")
        print("{}{}".format(firstname, lastname))