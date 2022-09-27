# fullname = "Vincent Oke"
# print(fullname)

firstname = "Vincent"
middlename = "Segun"
lastname = "Oke"

# CONCATENATION
# fullname = firstname + " " + middlename + " " + lastname
# print(fullname)

# F-STRINGS
# fullname = f"{firstname} {middlename} {lastname}"
# print(fullname)


# print(f"{firstname} {middlename} {lastname}")

# print(len(f"{firstname} {middlename} {lastname}"))

fullname = f"{firstname} {middlename} {lastname}"
print(fullname)
print(len(fullname))
print(len(firstname))
print(len(middlename))
print(len(lastname))

print(f"{len(firstname)} {len(middlename)} {len(lastname)}")

# USING FORMAT FUNTION
print(format(fullname))
print(format(firstname))


# x = 7
# y = 9
# sum = x + y
# print(sum)

# # We have two variables "firstname" and "lastname", let's say we want to print the full name on the console
# # How do we do that?

# # We can do it like below:

# fullname = first + " " + last

# # The "+" operator in the case of strings is for CONCATENATION

# print(fullname)

# # Using concatenation is OK, but there is a better approach to do this in Python
# # We can use Formatted Strings. Formatted strings are expressions gets evaluated at run-time

# fullname = f"{first} {last}"
# print(fullname)

# # You can put any valid expressions in between the curly braces
# # For example:

# fullname = f"{len(first)} {last}"
# print(fullname)

# fullname = f"{len(first)} {2 + 2}"
# print(fullname)
