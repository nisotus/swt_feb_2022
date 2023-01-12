# SQLite allows us to easily store our data in a structured format, like a table of rows and columns
# To work with SQLite in Python, we need to import the "sqlite3" module

# import sqlite3

# In the last session we created the "movies.json" file
# So we will read all the movies from the json file and store them in a SQLite database
# So we also need to import the "json" module

# import json

# We also need to import the class "Path" from the "pathlib" module

# from pathlib import Path

# movies = json.loads(Path("movies.json").read_text())

# print(movies)

# *** Storing data in a database
# with sqlite3.connect("db.sqlite3") as conn:
     # Let's assume we have a table called "Movies" where we store all our movies
     # Then we add values - "VALUES(?, ?, ?)" - The question marks are placeholders
     # So our table of "Movies" will have three columns "id", "title" and "year",
     # command = "INSERT INTO Movies VALUES(?, ?, ?)"
     
    # command = "INSERT INTO Movies VALUES(?, ?, ?)"
    # for movie in movies:
    #     conn.execute(command, tuple(movie.values()))
         
    # conn.commit()

# If we run this program, our database file will be created
# but we are going to get an error - "sqlite3.OperationalError: no such table: Movies"
# We get the "operational error" because we are delaing with an empty database, the database does not have any tables
# So we need to create the "Movies" TABLE first
# For this we need to download and install from here: https://sqlitebrowser.org/

# *** DB Browser for SQLite
# Launch "DB Browser for SQLite" and click on "Open Database"
# Select our database file
# Select "Create Table"
# Enter "Movies" as Table name
# Click "Add Field" and add three fields/columns
# "Id" - Type: INTEGER, Mark it as Primary Key = PK - Unique identifier for each movie
# "Title",  Type: TEXT
# "Year", Type: INTERGER
# Click "OK"

# Now inspect the "Movies" table and all the columns you have just created

# Click "Write Changes"

# *** Back to our program
# Let's run our program one more time
# Notice that this time we did not get an error

# # *** Back to our program
# # Now if we go back to "DB Browser for SQLite" and select the "Movies" table and go to "Browse Data"
# # You will see both our movies ended up in the database and they are stored in a structured format

# # So our program will look like below:

# import sqlite3
# import json
# from pathlib import Path


# with sqlite3.connect("db.sqlite3") as conn:
#     command = "SELECT * FROM Movies"
#     cursor = conn.execute(command)
#     for row in cursor:
#       print(row)
      
# We also have the method "fetchall()" that would return all the rows in the table in one go
    # movies = cursor.fetchall()
    # print(movies)
    
# If we run this we are not going to get any result
# Because after we iterate over the cursor = " for row in cursor: print(row)"
# We'll get to the end of the cursor, so we won't be able to read it again

# But if we comment out the iteration over the cursor, then we will get some result when we run the program

import sqlite3
import json
from pathlib import Path


with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    
    movies = cursor.fetchall()
    print(movies)
    
# So this is the basics of working with SQLite Databases in Python
# When working with dtabases, you should be familiar with SQL Programming language