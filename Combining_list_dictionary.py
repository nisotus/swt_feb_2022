
breakfast = ["Egg sandwitch", "Bagel", "Coffee"]
lunch = ["BLT", "PB&J", "Turkey sandwitch"]
dinner = ["Soup", "Salad", "Spaghetti", "Taco"]

#Combined to a list of list
menu = [["Egg sandwitch", "Bagel", "Coffee"],
        ["BLT", "PB&J", "Turkey Sandwitch"],
        ["Soup", "Salad", "Spaghetti"]]

#getting a list from a list
print("Breakfast Menu:\t", menu[0])
print("Lunch Menu:\t", menu[1])
print("dinner menu:\t", menu[2] )

#getting individual item from a 2 dimensional list list
print(menu[0])
print(menu[0][1])

#Instead of using a list, we can also use a dictionary for our menus with keys for Breakfast, Lunch, Dinner.

menu= {"breakfast" : ["Egg sandwitch", "Bagel", "Coffee"],
"lunch" : ["BLT", "PB&J", "Turkey sandwitch"],
"dinner" : ["Soup", "Salad", "Spaghetti", "Taco"]}
#To print each menu list, you can use the key to acess each list
print("breakfast menu:\t", menu["breakfast"])
print("lunch menu:\t", menu["lunch"])
print("dinner menu:\t", menu["dinner"])
#using a dictionary key and value in for loop

for item in menu:
    print(item)                 #It printed out just the key here
    
for name, menu in menu.items():
    print(name, ":", menu)        #it printed out both the key and values
    

#using dictionaries to represent objects

person = {"name": "Sarah smith",
          "city": "Orlando",
          "age": "100"}
#To print out how old the person is
print(person.get("name"), "is", person.get("age"), "years old.")
    
    
    
    
#We can also use dictionary to represent object
contact = {
    "number":4,
    "students":
     [
    {"name" : "sarah holderness", "email": "sarah@example.com"},
    {"name" : "harry potter", "email": "harry@example.com"},
     {"name": "Hermoine Granger", "email":"hermoine@example.com"},
     {"name" : "Ron Weasley", "email": "ron@example.com"}
     ]
}
#to get the students info in the comtact:
for student in contact["students"] :      ##i.e for student inside the contact, bring out students.
    print(student)
    
#to get the email of just the students: 
for student in contact["students"] :
    print(student["email"])