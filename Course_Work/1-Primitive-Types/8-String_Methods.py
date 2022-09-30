car1 = "volvo"
car2 = "TOyoTA"
car3 = "MerCeDes"
car4 = "Lambourghini is a very fast car"
car5 = "      Hummer Jeep      "
car6 = "   Nissan is a very good car    "


# len(car)
# print(car)
# print(len(car))

# Using upper()
print(car1.upper())

# Using lower()
print(car2.lower())

# Using capitalize()
print(car3.capitalize())

# Using title()
print(car4.title())

# Using strip()
print(car5.strip())

# Using rstrip() and lstrip()
print(car6.rstrip())
print(car6.lstrip())

# Finding character position
my_people = "All my people are pro in playing soccer"
print(my_people.find("pro"))

print(my_people.find("holy"))

# Using replace
my_people = "All my people are pro in playing soccer"
print(my_people.replace("pro", "amateur"))

# Checking the existence of a character or sequence of characters in a string
fun_things = "Reading comic books and swimming"
print("comical" in fun_things)

print("comic" not in fun_things)
