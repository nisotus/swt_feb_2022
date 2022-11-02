# Write a program to find the largest number in a LIST
# numbers = [1, 10, 50, 25, 81, 150]

# Use a function to write the same code

<<<<<<< HEAD
# list of number = [1, 10, 50, 25, 81, 150

# print the largest number
print("largest number")
=======
num = [1, 10, 50, 25, 81, 150]
def max_number(num):
    print(max(num))
    
max_number(num)


#*********************************


numbers = [1, 10, 50, 25, 81, 150]
def max_num(numbers):
    max = numbers[0]
    
    for x in numbers:
        if x > max:
            max = x
            
    return max

print("Largest number in list is: ", max_num(numbers))
>>>>>>> 016fdcc334b06116fdeb7a0b1bd87a7a665a1a71
