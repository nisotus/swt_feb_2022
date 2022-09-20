# Write a Python program that will print all English alphabets to the terminal
# Then use all the alphabets to print out the names of 4 members of your family

# PSEUDOCODE
# I need to save all English alphabets in a variable or in some type of way
# I need to access the position of the alphabets that spells the name of the person I want spell
# Then I need to save that name somewhere
# Then I need to print it out



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
