# The code below has two exceptions.
# I want you to handle both exceptions using try/except block
# Also decide on the best place to put the finally clause



# my_list = [1,2,3,4,5,6,7]
# file = open("Assigment37.py")
# for num in my_list:
#     print(num * 10)
#     if num % 0 == 0:
#         print("Number divisble by 10")
#     else:
#         print("Number not divisible by 10")
# file.close()




####code solution:

try:
    my_list = [1, 2, 3, 4, 5, 6, 7]
    file = open("Assignmenr37.py")
    for num in my_list:
        print(num * 10)
        if num % 0 == 0:
            print("Number divisible by 10")
        else:
            print("Number not divisible by 10")
except (FileNotFoundError, NameError):
    print("You are not in your right directory path")

finally:
    file.closed() 
   





