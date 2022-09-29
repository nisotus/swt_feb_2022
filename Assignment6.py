# Write a Python program that will take the string below as input and split/separate the alphabets from the numbers
# "My name is Will Brown and I am 48 years old, but my daughter is 17"


# def splitString(str):
 
#     alpha = ""
#     num = ""
#     special = ""
#     for i in range(len(str)):
#         if (str[i].isdigit()):
#             num = num+ str[i]
#         elif((str[i] >= 'A' and str[i] <= 'Z') or
#              (str[i] >= 'a' and str[i] <= 'z')):
#             alpha += str[i]
#         else:
#             special += str[i]
 
#     print(alpha)
#     print(num )
#     print(special)

# if __name__ == "__main__":

     
#     str = "geeks01$$for02geeks03!@!!"
#     splitString(str)

alph =[]
num = []
str_inp = (input('enter a string of characters :'))
for i in range(len(str_inp)):
    if (str_inp[i].isdigit()):
        num.append(str_inp[i])
    else:
        ((str_inp[i] >= 'A' and str_inp[i] <= 'Z')) 
        ((str_inp[i] >= 'a' and str_inp[i] <= 'z'))
        alph.append(str_inp[i])
print(num)
print(alph)

     
 








# res1 = []
# res2 = []
# while True:
#     str_inp = str(input('enter a string of characters :'))
#     if str_inp == 'done':
#         break
#     for letter, digit in str_inp:
#         if chr == 'letter':
#             res1.append(letter)
#         if chr == 'digit':
#             res2.append(digit)
# print(res1)
# print(res2)

    


   

        









# new_list = list()
# str_inp = str(input('enter a string of characters :'))
# for x in str_inp:
#     x == int('x')
#     for y in str_inp:
#         y == str('y')
#         new_str = str_inp.rsplit(y)
#         new_int = str_inp.lsplit(x)
#         new_list.append(new_str + new_int)
# print(new_list)

   




  

# index1 = str_inp.find('8')
# index2 = str_inp.find('15')
# print(int(index1))
# print(int(index2))

# def text_num_split(item):
#     for index, letter in enumerate(item, 0):
#         if letter.isdigit():
#             return [item[:index],item[index:]]

# print(text_num_split("foobar12345"))







