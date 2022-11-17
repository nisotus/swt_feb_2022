# In Python we have 3 logical operators and we use these operators to model more complex conditions

# These operators are:
# **********************
# and
# or
# not

# Imagine we are building an application for processing loans
# If the applicant has high income and good credit score, then they are eligible for the loan

# high_income = True
# good_credit = True

# if high_income and good_credit:
#     print("Eligible")
# else:
#     print("Not Eligible")

# With "and" operator:
# if both conditions are True, the result will be True
# if one of the conditions is False, the result will be False

# high_income = True
# good_credit = False

# if high_income and good_credit:
#     print("Eligible")
# else:
#     print("Not Eligible")

# With "or" operator:
# As long as at least one of the conditions is True, the result will be True

# high_income = True
# good_credit = False

# if high_income or good_credit:
#     print("Eligible")
# else:
#     print("Not Eligible")

# With "not" operator:
# The "not" operator basically inverses the value of a Boolean.
# If True it changes it to False and if False it changes it to True

# high_income = True
# good_credit = True
# student = True

# if not student:
#     print("Eligible")
# else:
#     print("Not Eligible")


# If student = False
# The the result will be True
# high_income = True
# good_credit = True
# student = False

# if not student:
#     print("Eligible")
# else:
#     print("Not Eligible")
    

# Here is an example. 
# A person can be eligible if they have either high income or good credit and they should not be student
# How do we implement this condition?

# high_income = True
# good_credit = False
# student = False

# if (high_income or good_credit) and not student:
#     print("Eligible")
# else:
#     print("Not Eligible")


# So with these operators, you can model all kinds of real world scenarios

# high_income = 20000
# good_credit = 4

# income = float(input("Enter the income: "))
# credit_score = int(input("Enter the credit score: "))
# student = input("Enter 'Yes' if student and 'No' if not student: ")

# if (income > 20000 or credit_score >= 4 and credit_score <= 5) and student == "Yes": 
#     print("Eligible")
# else:
#     print("Not Eligible")