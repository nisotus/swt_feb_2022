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







customers_name = input("Enter your name: \n")
wash_level = input("Enter the wash level you want to perform: \n")

car_size = input("Enter the size of your car: \n")

Normal = int(1000)
Basic = int(2000)
Gold = int(3000)
Platinum = int(4000)

small = int(10)
medium = int(20)
large = int(30)


#Assignment 15


payment_amount = int(wash_level) * int(car_size)
print(payment_amount)


