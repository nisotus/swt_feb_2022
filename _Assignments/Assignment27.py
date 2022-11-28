# Write a Python program that prints out the whole clandar month of a particular year to the terminal



###code########

import calendar

calendar_year = int(input("Enter the calendar year: "))
month= int(input("Enter the calendar month: "))

x = calendar.calendar_year(calendar_year, month)
print(x)