# Starting with the sample code above. Find a way to renmove all elements in the list by using a LOOP and the pop() method.
# Do not use any other approach, you have to use a LOOP in combination with the pop() method.


letters = ["a", "b", "c", "b", "d" , "b", 1, 2, 6, 7, 10]

while letters != []:
    letters.pop()

print(letters)