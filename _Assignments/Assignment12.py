# Write a Python program that will take as input a value in SEK
# Convert the SEK to Naira equivalent
# Print the result in a very intuitive manner to the terminal

print ("Simple SEK to Naira Converter")
amount = ''
RATE = 39.18
while not amount.isdigit():
    amount = input("Enter amount in Kr: ")

sek = float(amount)
naira = sek * RATE
print(f'{sek:.2f} SEK is {naira:.2f} naira')

print(f'{(float(amount)):.2f} SEK is {(float(amount) * RATE):.2f} naira')