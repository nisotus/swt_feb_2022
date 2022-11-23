# Write a Python program that can convert between any two currencies that you input from the terminal
# ****************************************
# Request for the customer's fullname and print it to the terminal
# Request for the customer's ID number and create a conditional to verify if the ID number is valid
# If the ID number is valid, do the following:
# Ask which currency the customer will like to convert from? Take the response as input from the terminal
# Ask which currency the customer will like to convert to? Take the response as input from the terminal

# Based on the two currencies entered by the customer, perform currency conversion using the current live exchange rate
# Print the conversion amount to the terminal

# To get a live currency rate, you might need to use an API or any library that can help you to get live exchange rate online.


import requests


base_currency = input("Enter the base currency: ")
new_currency = input("Enter the new currency: ")
new_currency = "USD"

start_date = "2022-11-15"
end_date = "2022-11-16"


url = "https://api.exchangerate.host/timeseries?base={0}&start_date={1}&end_date={2}&symbols={3}".format(base_currency, start_date, end_date, new_currency)
    
response = requests.get(url)
data = response.json()
print(data)
   