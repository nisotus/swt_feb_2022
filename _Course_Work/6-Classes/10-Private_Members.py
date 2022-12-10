class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)

cloud = TagCloud()

cloud.add("python")
cloud.add("Python")
cloud.add("Python")
cloud.add("PythON")
cloud.add("PYTHON")

print(cloud["Python"])

print(cloud["PYTHON"])

# print(cloud.__tags["Python"])

# In case "rope" is not installed for you
# Please see solution here - https://stackoverflow.com/questions/48466151/python-refactoring-fails-in-visual-studio-code 
# pip3 install rope
# pip install rope

# "__dict__" is a DICTIONARY that holds all the attributes in a class
# Let's take a look

print(cloud.__dict__)
print(cloud._TagCloud__tags)

# In Python unlike languages like C# or Java, we don't really have the concept of PRIVATE MEMBERS
# These private members are still accessible from the outside
# Using double underscores is more of a convention to prevent accidental access of the private members