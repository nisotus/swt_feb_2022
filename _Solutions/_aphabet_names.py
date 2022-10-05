alphabets = "abcdefghijklmnopqrstuvwxyz"
print(alphabets)

# Printing Roseline
# name1 = alphabets[17] + alphabets[14] + alphabets[18] + alphabets[4] + \
#     alphabets[11] + alphabets[8] + alphabets[13] + alphabets[4]

# print(name1.capitalize())

# # Printing Vivien
# print(alphabets[21].upper() + alphabets[8] +
#       alphabets[21] + alphabets[8] + alphabets[4] + alphabets[13])

# # Printing Helen
# print(alphabets[7].upper() + alphabets[4] +
#       alphabets[11] + alphabets[4] + alphabets[13])

# # Printing Agnes
# print(alphabets[0].upper() + alphabets[6] +
#       alphabets[13] + alphabets[4] + alphabets[18])

first_letter_index = alphabets.find("r")
print(first_letter_index)

second_letter_index = alphabets.find("o")
print(second_letter_index)

third_letter_index = alphabets.find("s")
print(third_letter_index)

print(alphabets[first_letter_index] +
      alphabets[second_letter_index] + alphabets[third_letter_index])
