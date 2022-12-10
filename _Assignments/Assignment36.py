# # Time for an exercise!!!

# # # This is a very interesting exercise
# # # It is a common programming task that big companies like Amazon, Microsoft, Google use a LOT

# # # So let's say we have some text like below:

# # sentence = "This is a common interview question"

# # # I want you to write a program to find the most repeated character in the text


from collections import Counter

sentence = ("thisisacommoninterviewquestion")
print(sentence)
Counter()
result= Counter(sentence)
result = max(result, key=result.get)

print("Most frequent character: ",result)
