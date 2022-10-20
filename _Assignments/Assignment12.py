# Write a Python program that will take as input a value in SEK
# Convert the SEK to Naira equivalent
# Print the result in a very intuitive manner to the terminal

# sek = str(input("Enter the currency you want to convert: \n"))
# naira = str(input("Enter the new currency you wnt to convert to: \n"))

# exchange_rate = float(input("Enter the exchange rate of sek to naira: \n"))

# amount = float(input("Enter the amount that you want to convert: \n"))

# naira = exchange_rate * amount
# print("the naira value is ", naira  , "naira")


# #code

import requests
import json
import pprint

base = "USD"
new_currency = "NGN"

start_date = "2022-10-01"
end_date = "2022-10-01"






customers_name = input("Enter the customer's full name: \n")
Customers_id = input("Enter the customer's id: \n")

Customers_id = True

if Customers_id == True:
    base = (input("Which currency will you like to change?: \n"))
    new_currency = (input("Enter the new currency you will like to convert to?: \n"))
    url = 
    response = requests.get(url)
    data = response.json()
    print(data["rates"])

    
    
    
    
    
    
    
    





