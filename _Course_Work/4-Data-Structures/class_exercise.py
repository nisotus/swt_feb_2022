
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
    
#     def __iter__(self):
#         return iter(self.tags)

            
# cloud = TagCloud()
# cloud["python"] = 10
# cloud["python"]
# cloud.add("Python")
# cloud.add("pyThon")
# cloud.add("python")
# cloud.add("Java")
# cloud.add("vincent")
# print(cloud.tags)
# print(cloud["python"])
# print(len(cloud.tags))



###Practice exercise:

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
    
#     def __iter__(self):
#         return iter(self.tags)
    
    
# cloud = TagCloud()
# cloud.add("Python")
# cloud.add("Python")
# print(cloud["Python"])

# # print(cloud.__tags["Python"])

# print(cloud.__dict__)




# class Product:
#     def __init__(self, price):
#         self.__price = price
        

# # to make price private

#     def get_price(self):
#         return self.__price
#     def set_price(self, price): 
#         if price < 0:
#             raise ValueError("Price cannot be negative")
#         self.__price 

# # product1 = Product(-50)
# # print(product1.get_price())
# # print(product1.set_price(-50))


# #####Method 2

# #price = property(get_price, set_price)

# product1 = Product(10)
# print(product1.__price)


# **************************

class Product:
    def __init__(self, price):
        self.set_price(price)
        

# to make price private

    def get_price(self):
        return self.__price
    
    def set_price(self, value): 
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value
    
    price = property(get_price, set_price)


product1 = Product(10)
print(product1.price)









    
    