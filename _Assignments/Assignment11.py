# Convert below code using Chaining Comparison Operators

score = float(input("Enter Student Score: "))
#if score >= 0 and score < 40:
if 0 <= score < 40:
    print("Student Grade is F")

#elif score >= 40 and score < 50:
elif 40 <= score < 50:
    print("Student Grade is D")

#elif score >= 50 and score < 65:
elif 50 <= score < 65:
    print("Student Grade is C")

#elif score >= 65 and score < 75:
elif 65 <= score < 75:
    print("Student Grade is B")

#elif score >= 75 and score <= 100:
elif 75 <= score <= 100:
    print("Student Grade is A")
else:
    print("Invalid Score")