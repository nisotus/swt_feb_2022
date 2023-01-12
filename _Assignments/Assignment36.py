# Time for an exercise!!!

# This is a very interesting exercise
# It is a common programming task that big companies like Amazon, Microsoft, Google use a LOT

# So let's say we have some text like below:

sentence = "This is a common interview question"

# I want you to write a program to find the most repeated character in the text

all_freq = {}
for i in sentence:
 if i in all_freq:
  all_freq[i] += 1
 else:
  all_freq[i] = 1
res = max(all_freq, key = all_freq.get)
 
# printing result
print ("The maximum of all characters in This is a common interview question is : " + str(res))


# # Python 3 code to demonstrate
# # Maximum frequency character in String
# # collections.Counter() + max()
# from collections import Counter
 
# # initializing string
# test_str = "GeeksforGeeks"
 
# # printing original string
# print ("The original string is : " + test_str)
 
# # using collections.Counter() + max() to get
# # Maximum frequency character in String
# res = Counter(test_str)
# res = max(res, key = res.get)
 
# # printing result
# print ("The maximum of all characters in GeeksforGeeks is : " + str(res))
