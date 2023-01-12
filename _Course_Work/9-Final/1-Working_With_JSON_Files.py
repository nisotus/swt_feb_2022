# These days, it's important to know JSON because a lot of popular websites like
# Facebook, Twitter, Yelp, YouTube, etc... provide their data in JSON format
# Also if you have a website, you can provide your data in JSON format

# API - Application Programming Interface

# So let's see how to work with JSON files

# First step is to import "json" module

import json
from pathlib import Path

# movies = [
#     {"id": 1, "title": "Terminator", "year": 1989},
#     {"id": 2, "title": "Kindergaten Cop", "year": 1993}
# ]

# data = json.dumps(movies)

# print(data)
# print(movies)

# *** Writing data to a JSON file
# Path("movies.json").write_text(data)

# Run the program and we will now have "movies.json" in our project folder
# So we have learnt how to write data to a JSON file

# Path("movies.json").write_text(data)

# *** Reading data from a JSON file
# Now let's imagine that we get a JSON file from somewhere else
# This could be the data we get form Faceboook, Twitter, IMDB, Yelp, YouTube etc...
# So we should be able to read this data in Python

data = Path("movies.json").read_text()

movies = json.loads(data)
print(movies)

print(movies[0])

print(movies[0]["title"])
