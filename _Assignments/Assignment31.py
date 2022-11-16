# Write a Python program that randomly rearrange or shuffle the items in the list below:


# Randomly rearranging the order of items in a sequence (Shuffling the items of a sequence in place)
deck = ["Ace", "Two", "Three", "Four", "Five", "Six",
        "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

#code

import random

deck = ["Ace", "Two", "Three", "Four", "Five", "Six",
        "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

deck_shuffle=(random.shuffle(deck))
print(deck)

print(deck_shuffle)
