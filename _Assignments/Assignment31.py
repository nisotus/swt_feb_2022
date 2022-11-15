# Write a Python program that randomly rearrange or shuffle the items in the list below:


# Randomly rearranging the order of items in a sequence (Shuffling the items of a sequence in place)
deck = ["Ace", "Two", "Three", "Four", "Five", "Six",
        "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

import random

def myfunction() :
        return 0.1


mylist = ["Ace", "Two", "Three", "Four", "Five", "Six",
        "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

random.shuffle(mylist,myfunction)
print(mylist)


random.shuffle(mylist)
print(mylist)