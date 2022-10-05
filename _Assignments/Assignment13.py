# Write a Python program that will take as input a value in celcius
# Convert the value to Farenheit
# Print the result in a very intuitive manner to the terminal


celcius_value = float(input("Enter the celcius value: \n"))
conversion = celcius_value * 1.8 + 32
print("The fahrenheit value is ", conversion)
