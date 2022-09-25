# Write a Python program that will print all English alphabets to the terminal
# Then use all the alphabets to print out the names of 4 members of your family

# PSEUDOCODE
# I need to save all English alphabets in a variable or in some type of way
# I need to access the position of the alphabets that spells the name of the person I want spell
# Then I need to save that name somewhere
# Then I need to print it out


<<<<<<< HEAD:Assignment3.py
A  lphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(Alphabet_list)
first_letter = Alphabet_list[14]

second_letter = Alphabet_list[11]

third_letter = Alphabet_list[20]

fourth_letter = Alphabet_list[12]

fifth_letter = Alphabet_list[8]

sixth_letter = Alphabet_list[3]

seventh_letter = Alphabet_list[4]

fullname = first_letter + second_letter + third_letter + fourth_letter + fifth_letter + sixth_letter + seventh_letter


print(fullname)

fullname = f"{first_letter} {second_letter} {third_letter} {fourth_letter} {fifth_letter} {sixth_letter} {seventh_letter}"

print(fullname)
=======

letter = "a"
while True:
    print(letter)
    numLetter = ord(letter)
    if letter == "z":
         break
    numLetter = numLetter + 1
    letter = chr(numLetter)
print(letter)

letter = 'abcdefghijklmnopqrstuvwxyz'
names = []
name_1 = ('tomilayo')
name_2 = ('muyiwa')
name_3 = ('tise')
name_4 = ('tiyin')
for name in letter:
    names.append([name_1, name_2, name_3, name_4])   
print(names)
>>>>>>> main:Course_Work/Assignment3.py
