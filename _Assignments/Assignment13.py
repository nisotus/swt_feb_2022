# Write a Python program that will take as input a value in celcius
# Convert the value to Farenheit
# Print the result in a very intuitive manner to the terminal
print ("Celsuis to Farenheit Converter")
temperature = ""

while not temperature.isdigit():
    temperature = input("Enter the present temperature: ")

farenheit = (int(temperature) * 9 / 5) + 32
print(f'It\'s {farenheit}ºF')