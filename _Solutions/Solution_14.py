# Write a Python program for a car wash system
# The car wash has 4 levels of washing (Normal, Basic, Gold, Platinum)
# The cost is calculated based on the level and the car size (Small, Medium, Large)

# I want you to think of an approach to to implement this solution by using prices (for the different levels) and numbers for the car size.
# You will need to multiply these values to get a washing cost
# You need to take all the values that is needed as input and display the final cost based on the input from the customer

# Name
# Level
# size
# payment amount

# *** Levels of car wash
level_1 = "Normal"
level_2 = "Basic"
level_3 = "Gold"
level_4 = "Platinum"

# *** Prices per level
price_level_1 = 100
price_level_2 = 150
price_level_3 = 200
price_level_4 = 300

# *** Car sizes
car_size_1 = "Small"
car_size_2 = "Medium"
car_size_3 = "Large"

# *** Prices per car size
price_size_small = 20
price_size_medium = 30
price_size_large = 50


level = input("""***Enter the LEVEL for your car wash today:
              Input one value from below:
              *** Normal
              *** Basic
              *** Gold
              *** Platinum
              *** : """)
car_size = input("""Enter the SIZE of your car:
                 *** Small
                 *** Medium
                 *** Large
                 *** : """)

level = level.capitalize()
car_size = car_size.capitalize()

# total_price = 0

if level == "Normal" and car_size == "Small":
    total_price = price_level_1 * price_size_small
    print(f"Your total price for your car wash today is", total_price)
elif level == "Normal" and car_size == "Medium":
    total_price = price_level_1 * price_size_medium
    print(f"Your total price for your car wash today is", total_price)
elif level == "Normal" and car_size == "Large":
    total_price = price_level_1 * price_size_large
    print(f"Your total price for your car wash today is", total_price)
elif level == "Basic" and car_size == "Small":
    total_price = price_level_2 * price_size_small
    print(f"Your total price for your car wash today is", total_price)
elif level == "Basic" and car_size == "Medium":
    total_price = price_level_2 * price_size_medium
    print(f"Your total price for your car wash today is", total_price)
elif level == "Basic" and car_size == "Large":
    total_price = price_level_2 * price_size_large
    print(f"Your total price for your car wash today is", total_price)
elif level == "Gold" and car_size == "Small":
    total_price = price_level_3 * price_size_small
    print(f"Your total price for your car wash today is", total_price)
elif level == "Gold" and car_size == "Medium":
    total_price = price_level_3 * price_size_medium
    print(f"Your total price for your car wash today is", total_price)
elif level == "Gold" and car_size == "Large":
    total_price = price_level_3 * price_size_large
    print(f"Your total price for your car wash today is", total_price)
elif level == "Platinum" and car_size == "Small":
    total_price = price_level_4 * price_size_small
    print(f"Your total price for your car wash today is", total_price)
elif level == "Platinum" and car_size == "Medium":
    total_price = price_level_4 * price_size_medium
    print(f"Your total price for your car wash today is", total_price)
elif level == "Platinum" and car_size == "Large":
    total_price = price_level_4 * price_size_large
    print(f"Your total price for your car wash today is", total_price)
else:
    print("Invalid input, unable to calculate price...")
