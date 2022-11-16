# Use DICTIONARY COMPREHENSION to rewrite below code:

vowels = {"a": 1, "e": 5, "i": 9, "o": 16, "u": 21}
for v, w in vowels.items():
    print(v, w * 2)
    
#code

vowels = {v: w*2 for v in vowels}
print(v)
