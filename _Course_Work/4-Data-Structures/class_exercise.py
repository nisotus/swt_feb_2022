
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
cloud["python"]
cloud.add("Python")
cloud.add("pyThon")
cloud.add("python")
cloud.add("Java")
cloud.add("vincent")
print(cloud.tags)
print(cloud["python"])
print(len(cloud.tags))


