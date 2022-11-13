# Using the list below:

shopping_cart = [
    ("Clipper", 1),
    ("Brush", 20),
    ("Laptop", 2)
    ("Pen", 150),
    ("USB-Type-C", 51),
    ("Jabra-Headset", 1000)
]


# # 1 Use the Lambda function to sort the items based on the prices in ascending order
# # 2 Use the Lambda function to sort the items based on the prices in descending order
# # 3 Use the Map function to get a list of the prices
# # 4 Use the Map function to get the prices without putting in a list
# # 5 Use the Filter function to filter prices greater than or equal to 150
# # 6 Use the Filter function to filter prices less than or equal to 20
# <<<<<<< HEAD

# =======
# # 7 Use LIST COMPREHENSION to filter prices less than or equal to 20
# 8 Use LIST COMPREHENSION to get the list of proces into another list
# >>>>>>> afaca3834adeecf357b8186750c35f1bf3b39e15

# shopping_cart = [
#     ("Clipper", 1),
#     ("Brush", 20),
#     ("Laptop", 2)
#     ("Pen", 150),
#     ("USB-Type-C", 51),
#     ("Jabra-Headset", 100) ]


# shopping_cart.sort (key=lambda item: item [1]) 

# prices = []

# for item in shopping_cart:
#     prices.append(item[1])
#  print(prices)   



shopping_cart = [
    ("Clipper", 1),
    ("Brush", 20),
    ("Laptop", 2)
    ("Pen", 150),
    ("USB-Type-C", 51),
    ("Jabra-Headset", 100) 
]

filtered = [item for item in shopping_cart if item [1] >=1]
print(filtered)

prices = [item [1] for item in shopping_cart]
prices.sort()
print(prices)