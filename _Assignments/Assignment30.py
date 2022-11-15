# Write a Python program that randomly selects and prints an item from below List

# Randomly select a movie
movies = ["Aladdin", "Stuber", "Pets 2", "Toy Story 4", "The Lion King",
          "Late Night", "Judgemental Hai Kya", "Once Upon a Time in Hollywood",
          "Spider-Man:Far From Home", "Avengers: Endgame",
          "John Wick: Chapter 3 - Parabellum", "Men in Black: International", ]


import random

movies_list =["Aladdin", "Stuber", "Pets 2", "Toy Story 4", "The Lion King",
          "Late Night", "Judgemental Hai Kya", "Once Upon a Time in Hollywood",
          "Spider-Man:Far From Home", "Avengers: Endgame",
          "John Wick: Chapter 3 - Parabellum", "Men in Black: International", ]

movies = random.choice(movies_list)
print(movies)


