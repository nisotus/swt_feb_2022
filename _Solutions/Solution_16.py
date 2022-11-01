# One of the questions that usually come in programming interviews is the fizz/buzz algorithm
# You will be surprised that there are lots of programmers out there with even years of experience
# but they don't know how to solve this simple programming problem.

# So let's see how the algorithm works and you can spend 10 - 15 minutes to solve it on your own

# Here we have a function fizz_buzz()
# The function takes some input and depending on the input we give it
# It returns different results

# Here are the rules:3
# Rule 1: If the input that we give it is divisible by 3, it will return the string "Fizz"
# Rule 2: If the input that we give it is divisible by 5, it will return the string "Buzz"
# Rule 3: If the input that we give it is divisible by both 3 and 5, it will return the string "FizzBuzz"
# Rule 4: For any other numbers it will return the same input that you entered

def fizz_buzz(a):
    if (a % 3 == 0) and (a % 5 != 0):
        return "Fizz"
    elif (a % 5 == 0) and (a % 3 != 0):
        return "Buzz"
    elif (a % 3 == 0) and (a % 5 == 0):
        return "Fizz_Buzz"
    else:
        return a
    
print(fizz_buzz(15))

# a = 15
# b = 6

# print(a / b)
# print(a // b)
# print(a % b)
# print(a * b)
# print(a- b)
# print(a + b)


    