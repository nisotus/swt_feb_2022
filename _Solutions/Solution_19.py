# Write a program that calculates the SUM of all the items in a shopping cart
# Let's say we have a LIST of prices
# prices = [10, 20, 30]

# Use a function to write the same code

prices = [10, 20, 30]

def sum_prices(prices):
    # price = 0
    for price in prices:
        price = price + price
    return price

print((sum_prices(prices)))        