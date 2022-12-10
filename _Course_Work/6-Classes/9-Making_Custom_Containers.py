# We have learnt about the common data structures in Python
# LISTS
# SETS
# TUPLES
# ARRAYS
# DICTIONARIES
# and so on...

# They are called DATA STRUCTURES or CONTAINERS
# In most cases, they are useful and sufficient

# But there are times that you wnat to create your own CUSTOM CONTAINER TYPES

# For example, let us implement a class "TagCloud" from scratch together
# WIth a class "TagCloud" we want to keep track of the various tags on a blog

# For example, how many articles do we have that are tagged with the word "Python" or "JavaScript" or "Peter"

# class TagCloud:
#     pass

# We can create an instance of the "TagCloud" class and save it as "cloud"
# cloud = TagCloud()

# Since the "cloud" object is a container object, we can find the number of items in it 
# len(cloud)

# We can also get an item by it's key
# For example we can get the number of articles tagged with "python"
# cloud["python"]

# We can also set the number of articles to any integer value
# cloud["python"] = 10

# We can iterate over the container
# for tag in cloud:
#     print(tag)
    
####***Putting everything together

###*** This will fail***

# class TagCloud:
#     pass

# cloud = TagCloud()
# len(cloud)
# cloud["python"]
# cloud["python"] = 10
# for tag in cloud:
#     print(tag)
    
#**** How do you implement a class like this for it to work?

#*** Implementing a class

# class TagCloud:
#     def __init__(self):
#         self.tags = {}
    
#     def add(self, tag):
#         self.tags[tag] = self.tags.get(tag, 0) + 1
        
# cloud = TagCloud()
# cloud.add("python")
# cloud.add("python")
# cloud.add("python")
# print(cloud.tags)
 
 
# *** How do we handle caps and lower case situations?       

# class TagCloud:
#     def __init__(self):
#         self.tags = {}
    
#     def add(self, tag):
#         self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1
        
# cloud = TagCloud()
# cloud.add("Python")
# cloud.add("pythoN")
# cloud.add("pyThon")
# print(cloud.tags)

# *** let's take this to the next level = level 2

# class TagCloud:
#     def __init__(self):
#         self.tags = {}
    
#     def add(self, tag):
#         self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1
    
#     def __getitem__(self, tag):
#         return self.tags.get(tag.lower(), 0)
            
# cloud = TagCloud()
# cloud["python"]
# cloud.add("Python")
# cloud.add("pyThon")
# cloud.add("python")
# # print(cloud.tags)
# print(cloud["python"])

# *** let's take this to the next level = level 3

# class TagCloud:
#     def __init__(self):
#         self.tags = {}
    
#     def add(self, tag):
#         self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1
    
#     def __getitem__(self, tag):
#         return self.tags.get(tag.lower(), 0)
    
#     def __setitem__(self, tag, count):
#        self.tags[tag.lower()] = count
            
# cloud = TagCloud()
# cloud["python"] = 10
# cloud["python"]
# cloud.add("Python")
# cloud.add("pyThon")
# cloud.add("python")
# print(cloud.tags)
# print(cloud["python"])

# *** let's take this to the next level = level 4

# class TagCloud:
#     def __init__(self):
#         self.tags = {}
    
#     def add(self, tag):
#         self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1
    
#     def __getitem__(self, tag):
#         return self.tags.get(tag.lower(), 0)
    
#     def __setitem__(self, tag, count):
#        self.tags[tag.lower()] = count
       
#     def __len__(self):
#        return len(self.tags)
            
# cloud = TagCloud()
# cloud["python"] = 10
# cloud["python"]
# cloud.add("Python")
# cloud.add("pyThon")
# cloud.add("python")
# cloud.add("Java")
# print(cloud.tags)
# print(cloud["python"])
# print(len(cloud.tags))

# *** Now let's take this to the next level 5
# Finally, to make it iterable, so we can iterate over it using a FOR LOOP
# We need to implement another magic method called "__iter__"
# "__iter__" takes only the self parameter and all we have to do
# is to use one of the built-in functions called "iter" to get an iterator object
# An iterator object is an object that walks a container and gets one item at a time
# So in the "__iter__" method we return the "iter" function and pass "(self.tags)"
# "iter(self.tags)" returns an iterator object which gives us one item at a time in a FOR LOOP

class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud["python"] = 10
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)
print(cloud["python"])
print(len(cloud.tags))