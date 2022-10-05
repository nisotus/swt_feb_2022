import string

# Write a Python program that will print all English alphabets to the terminal
# Then use all the alphabets to print out the names of 4 members of your family

# PSEUDOCODE
# I need to save all English alphabets in a variable or in some type of way
# I need to access the position of the alphabets that spells the name of the person I want spell
# Then I need to save that name somewhere
# Then I need to print it out

names_file = (r'Siblings_Names.txt')            # text file with list of names
names = []                                      # empty list to read, for storing contents of text file above
processed_names = []                            # empty list to store names of generated by the program
indexes = []

temp = open(names_file, 'r')                    # open the text file with names

x = temp.readline()                             # read and save contents of opened file to names
while x != '':
    names.append(x.rstrip('\n'))
    x = temp.readline()

alphabets = list(string.ascii_letters)          # create a list of all English alphabets

# check the names proovided, and search for letters from the alphabet to form the names
for name in names:
    processed_names.append('')
    for letter in name:
        for char in alphabets:
            if char == letter:
                indexes.append((char, alphabets.index(letter)))
                processed_names[-1] += char

# Task 1: print each English alphabet
print(alphabets)
# Task 2: print names of 4 family members
for name in processed_names:
    print(name)
print(indexes)