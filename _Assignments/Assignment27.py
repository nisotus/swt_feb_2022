# Write a Python program that prints out the whole clandar month of a particular year to the terminal

import calendar
year = int(input("enter the year: "))
month = int(input("Enter the month: "))
x=calendar.month(year, month)

print("The calendar of the respective year is ", x)