# Using the list below:

shopping_cart = [
    ("Clipper", 1),
    ("Brush", 20),
    ("Laptop", 2),
    ("Pen", 150),
    ("USB-Type-C", 51),
    ("Jabra-Headset", 1000)
]


# 1 Use the Lambda function to sort the items based on the prices in ascending order
# 2 Use the Lambda function to sort the items based on the prices in descending order
# 3 Use the Map function to get a list of the prices
# 4 Use the Map function to get the prices without putting in a list
# 5 Use the Filter function to filter prices greater than or equal to 150
# 6 Use the Filter function to filter prices less than or equal to 20
# 7 Use LIST COMPREHENSION to filter prices less than or equal to 20
# 8 Use LIST COMPREHENSION to get the list of proces into another list

####code solution######
#1
# shopping_cart.sort(key=lambda item:item[1])
# print(shopping_cart)

#3
# prices = list(map(lambda item:item[1], shopping_cart))
# print(prices)

#4
# prices = (lambda item:item[1], shopping_cart)
# print(prices)

#5
# filtered = list(filter(lambda item:item[1] >= 150, shopping_cart))
# print(filtered)


#6
# filtered = list(filter(lambda item:item[1] <= 20, shopping_cart))
# print(filtered)


#7. List comprehension

# filtered = [item for item in shopping_cart if item[1] <= 20]
# print(filtered)

#8. List comprehension

prices = [item[1] for item in shopping_cart]
print(prices)