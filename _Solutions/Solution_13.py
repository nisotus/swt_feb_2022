# Write a Python program that will take as input a value in celcius
# Convert the value to Farenheit
# Print the result in a very intuitive manner to the terminal

value_in_celcius = float(input("Enter value in degrees Celcius: "))
value_in_fahrenheit = (value_in_celcius * 9/5) + 32
print(f"Degrees in Fahrenheit is: {round(value_in_fahrenheit)}")


value_in_fahrenheit = float(input("Enter value in degrees Fahrenheit: "))
value_in_celcius = (value_in_fahrenheit - 32) * 5/9
print(f"Degrees in Celcius is: {round(value_in_celcius)}")
