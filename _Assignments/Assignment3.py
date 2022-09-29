# Write a Python program that will print all English alphabets to the terminal
# Then use all the alphabets to print out the names of 4 members of your family

# PSEUDOCODE
# I need to save all English alphabets in a variable or in some type of way
# I need to access the position of the alphabets that spells the name of the person I want spell
# Then I need to save that name somewhere
# Then I need to print it out
# print(alphabets[first_letter_index] +
#       alphabets[second_letter_index] + alphabets[third_letter_index])

alphabets = 'abcdefghijklmnopqrstuvwxyz'
print(alphabets)

fst_name_index1 = alphabets.find('t')
fst_name_index2 = alphabets.find('o')
fst_name_index3 = alphabets.find('m')
fst_name_index4 = alphabets.find('i')

name_1 = (alphabets[fst_name_index1] + alphabets[fst_name_index2] + alphabets[fst_name_index3] + alphabets[fst_name_index4])
print(name_1)

sec_name_index1 = alphabets.find('m')
sec_name_index2 = alphabets.find('u')
sec_name_index3 = alphabets.find('y')
sec_name_index4 = alphabets.find('i')
sec_name_index5 = alphabets.find('w')
sec_name_index6 = alphabets.find('a')

name_2 = (alphabets[sec_name_index1] + alphabets[sec_name_index2] + alphabets[sec_name_index3] + alphabets[sec_name_index4] + alphabets[sec_name_index5] + alphabets[sec_name_index6]) 
print(name_2)

thd_name_index1 = alphabets.find('t')
thd_name_index2 = alphabets.find('i')
thd_name_index3 = alphabets.find('y')
thd_name_index4 = alphabets.find('i')
thd_name_index5 = alphabets.find('n')

name_3 = (alphabets[thd_name_index1] + alphabets[thd_name_index2] +alphabets[thd_name_index3] + alphabets[thd_name_index4] + alphabets[thd_name_index5])
print(name_3)

fth_name_index1 = alphabets.find('t')
fth_name_index2 = alphabets.find('i')
fth_name_index3 = alphabets.find('s')
fth_name_index4 = alphabets.find('e')

name_4 = (alphabets[fth_name_index1] + alphabets[fth_name_index2] + alphabets[fth_name_index3] + alphabets[fth_name_index4])
print(name_4)

