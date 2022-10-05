# Write a Python program that will take as input a value in SEK
# Convert the SEK to Naira equivalent
# Print the result in a very intuitive manner to the terminal

exchange_amount = float(
    input("Please enter how much you will like to exchange from SEK to NGN: "))
exchange_rate = float(
    input("Enter the exchange rate for SEK to NGN for today: "))

naira_value = exchange_amount * exchange_rate

print("Your Naira Value will be NGN", naira_value)

proceed = input("Should we proceed with the exchange? Answer 'Yes' or 'No': ")

proceed = proceed.capitalize()

if proceed == "Yes":
    print("Your account has now been credited with NGN", naira_value)
else:
    print("Transaction Aborted")

print("Next Customer Please...")
