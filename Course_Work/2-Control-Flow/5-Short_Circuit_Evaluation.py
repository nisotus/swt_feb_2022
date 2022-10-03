# Below is the example from the last lecture

# A person is eligible for a loan if they have high income and good credit and they are not a student

high_income = True
good_credit = True
student = True

if high_income and good_credit and not student:
    print("Eligible")

# So if we have below:
# The evaluation will STOP at the argument - "high_income" even though it is the first argument in the expression.
# The remaining arguments will not be evaluated.

high_income = False
good_credit = True
student = True

if high_income and good_credit and not student:
    print("Eligible")

# We have the same concept of short-circuit with the "or" operator
# In the case below, the evaluation will STOP at - "good_credit" - since it is True

high_income = False
good_credit = True
student = True

if high_income or good_credit and not student:
    print("Eligible")