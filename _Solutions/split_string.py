# Write a Python program that will take the string below as input and split/separate the alphabets from the numbers
# "My name is Will Brown and I am 48 years old, but my daughter is 17"

import re

mystring = "My name is Will Brown and I am 48 years old, but my daughter is 17"
n=re.findall(r'\d',mystring)
a=re.findall(r'[a-zA-Z]',mystring)
print(n)
print(a)
print(" ".join(n))
print(" ".join(a))

# Solution from: https://www.codespeedy.com/separate-alphabets-and-numbers-in-a-string-using-regular-expressions-in-python/



aString = "My name is Will Brown and I am 48 years old, but my daughter is 17"
res = re.split('(\d+)', aString)
print(res)

bString = "My name is Will Brown and I am 48 years old, but my daughter is 17"
res = re.findall('(\d+|[A-Za-z]+)', bString)
print(res)
print(" ".join(res))


dstring= "My name is Will Brown and I am 48 years old, but my daughter is 17"
n=re.findall(r'\d*', dstring)
a=re.findall(r'[a-zA-Z]*', dstring)
print(n)
print(a)
