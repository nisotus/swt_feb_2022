# Using the list below:# 1 Use the Lambda function to sort the items based on the prices in ascending order
# 2 Use the Lambda function to sort the items based on the prices in descending order
# 3 Use the Map function to get a list of the prices
# 4 Use the Map function to get the prices without putting in a list
# 5 Use the Filter function to filter prices greater than or equal to 150
# 6 Use the Filter function to filter prices less than or equal to 20
# 7 Use LIST COMPREHENSION to filter prices less than or equal to 20
# 8 Use LIST COMPREHENSION to get the list of proces into another list




shopping_cart = [
    ("Clipper", 1),
    ("Brush", 20),
    ("Laptop", 2)
    ("Pen", 150),
    ("USB-Type-C", 51),
    ("Jabra-Headset", 1000)
    ]
    
prices =[item for item in shopping_cart if item[1]>=1]
print(prices)

prices = [item[1] for item in shopping_cart]
print.sort(prices)
print(prices)
