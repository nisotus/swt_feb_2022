# Write a Python program that will take the string below as input and split/separate the alphabets from the numbers
text = "My name is Will Brown and I am 48 years old, but my daughter is 17"
outputText = ""
numbers = []
for word in text.split(' '):
    if word.isdigit():
        numbers.append(int(word))
    else:
        outputText += (word + ' ')
print (outputText)
print (numbers)