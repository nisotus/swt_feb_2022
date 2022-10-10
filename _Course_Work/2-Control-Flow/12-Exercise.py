# Time for an exercise

# I want you to write a program to display the even numbers between 1 to 10
# So when you run this program, you should see 2, 4, 6, 8
# and after this I want you to print the message "We have 4 even numbers"

count = 0
for number in range(1, 50):
    if number % 2 == 0:
        count += 1
        print(number)

print(f"We have {count} even numbers")
