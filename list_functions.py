#List
from xml.dom.expatbuilder import InternalSubsetExtractor


acronyms = ["LOL", "IDK", "SMH"]

#append
acronyms.append("BFN")

print(acronyms)

#Method are called on the object.
#append
# acronyms.append("BFN")
# print(acronyms)

#delete
acronyms.remove("IDK")
print(acronyms)

# del acronyms[0]
# print(acronyms)

#To check if an item is in a list using an "if" statement

# if 1 in [1, 2, 3, 4, 5]:
#     print(True)
# else:
#     print("False")
    
#To check if the variable word is in acronyms list

# acronyms = ["LOL", "IDK", "SMH", "TBH"]
# word = "BFN"

# if word in acronyms:
#     print( word + " is in the list")
# else:
#     print(word + " is NOT in the list")
    
    
    
#To print each acronyms on a seperate line, we need a loop.

# A for loop looks similar to the if statement to check if an item is in a list.
# acronyms = ["LOL", "IDK", "SMH", "TBH"]

# for acronym in acronyms:
#     print(acronym)



#More examples on loop using "for" statement

# expenses = [10.50, 8, 5, 15, 20, 5, 3]
# sum = 0

# for x in expenses:
#     sum = sum + x
#     print("You spent $", sum, " on lunch this week", sep= "")
    
    
## We can skip the for loop and rather use a call function by calling the sum function(sum is also a python buit in function), and pass the expenses as argument.

# expenses = [10, 8, 5, 15, 20, 5, 3]
# total = sum(expenses)

# print("You spent $", total, " on lunch this week.", sep= "")


## Range and for loop

# total = 0
# expenses = []
# for i in range(7):
#    expenses.append(float(input("Enter an expense: ")))
# total = sum(expenses)
# print("You spent $", total, sep="")


#In a situation that the user has a number of expenses they want to sum up
# total = 0
# expenses = []
# num_expenses = int(input("Enter the value of expenses"))
# for i in range(num_expenses):
#     expenses.append(float(input("Enter an expense:")))
#     total = sum(expenses)
# print("You spent $", total, sep="")
    
    
    
## To create a loan calculator to calculate how much of our loan we paid off after a given number of months.

#Get the loan details:
money_owed = float(input("How much do you owe, in dollar?\n"))
apr = float(input("What is the annual percentage rate?\n"))
payment = float(input("What will your monthly payment be, in dollars??n"))
months = int(input("How many months do you want to see the result for?"))

#divide apr by 100 to make it a percent, then divide by 12 to know the monthy interest
monthly_rate = apr/100/12

# Add in interest
interest_paid = money_owed * monthly_rate
money_owed = money_owed + interest_paid

# Make payment
money_owed= money_owed + interest_paid

#print the result for this month
print("Paid", payment, "of which", interest_paid, "was interest", end=" ")
print("Now I owe", money_owed)




## now we want to add a loop that does this for as many months as the user wanted.

#Get the loan details:
money_owed = float(input("How much do you owe, in dollar?\n"))
apr = float(input("What is the annual percentage rate?\n"))
payment = float(input("What will your monthly payment be, in dollars??n"))
months = int(input("How many months do you want to see the result for?"))

#divide apr by 100 to make it a percent, then divide by 12 to know the monthy interest
monthly_rate = apr/100/12

for i in range (months):
# Add in interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid
    
    if (money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the loan in", i+1, "months")
        break

# Make payment
    money_owed= money_owed + interest_paid

#print the result for this month
    print("Paid", payment, "of which", interest_paid, "was interest", end=" ")
    print("Now I owe", money_owed)





    
    
    
    
