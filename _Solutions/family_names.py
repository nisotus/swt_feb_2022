# Write a Python program that will print all English alphabets to the terminal
# Then use all the alphabets to print out the names of 10 members of your family

alphabets = "abcdefghijklmnopqrstuvwxyz"
print(alphabets)

first_letter_position = alphabets.find("r")
print(first_letter_position)

second_letter_position = alphabets.find("o")
print(second_letter_position)

third_letter_position = alphabets.find("s")
print(third_letter_position)

fourth_letter_position = alphabets.find("e")
print(fourth_letter_position)

fifth_letter_position = alphabets.find("l")
print(fifth_letter_position)

sixth_letter_position = alphabets.find("i")
print(sixth_letter_position)

seventh_letter_position = alphabets.find("n")
print(seventh_letter_position)

eight_letter_position = alphabets.find("e")
print(eight_letter_position)

fullname = alphabets[first_letter_position].capitalize() + alphabets[second_letter_position] + alphabets[third_letter_position] + alphabets[fourth_letter_position] + alphabets[fifth_letter_position] + alphabets[sixth_letter_position] + alphabets[seventh_letter_position] + alphabets[eight_letter_position]

print(fullname)