# Write a Python program that will take as input a value in SEK
# Convert the SEK to Naira equivalent
# Print the result in a very intuitive manner to the terminal

sek = str(input("Enter the currency you want to convert: \n"))
naira = str(input("Enter the new currency you wnt to convert to: \n"))

exchange_rate = float(input("Enter the exchange rate of sek to naira: \n"))

amount = float(input("Enter the amount that you want to convert: \n"))

naira = exchange_rate * amount
print("the naira value is ", naira  , "naira")





