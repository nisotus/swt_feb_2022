# A dictionary is a key value pair. It maps key to values

acronyms = {"LOL": "laugh out loud",
            "TDK": "I dont know",
            "TBH" : "to be honest"}
print (acronyms)

print(acronyms["LOL"])
print(acronyms["TBH"])

# To update value in the dictionary
acronyms["TBH"] = "honesty"
print(acronyms["TBH"])

#To delete a value in the dictionary
del acronyms["LOL"]
print(acronyms)

#To get a value that might not be there anymore, it will give NONE.
definition = acronyms.get("BTW")

definition = acronyms.get("LOL")    #definition equals none because the key doesnt exist.
print(definition)       

#If definition has a value it will print definition, 

if definition:
    print(definition)
else:
    print("Key doesnt exist")
    
    
    
    
#Using a dictionary to translate a sentence

acronyms = {"LOL": "laugh out loud",
            "IDK": "I dont know",
            "TBH" : "to be honest"}

sentence = "IDK" + "what happened" + "TBH"
translation = acronyms.get("IDK") + "what happened" + acronyms.get("TBH")
print(sentence)
print(translation)

#To create a dictionary of a current movie showtime, and ask the user if they want to look up at a certain showtime. 

current_movies = {"The Grinch" : "11:00am",
                  "Rudolph": "1:00pm",
                  "Frosty the Snowman": "3:00pm",
                  "Christmas Vacacation": "5:00pm"}
print("We're showing the following movies: ")
for Key in current_movies:
    print(Key)
movie = input("what movie will you like the showtime for?")
showtime = current_movies.get(movie)
if showtime == None:
    print("The requested showtime is not playing")
else:
    print("movie is playing at showtime")
    



    