# from collections import Counter
# try:
#     file =  open('practice.txt','r')
#     word = file.read()
#     list_word= word.split(' ')
#     myDict = { v:dict(Counter(v)) for v in list_word}
#     print(myDict)
# except OSError:
#     print("Could not read file")

"""
{'Python': {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}, 'is': {'i': 1, 's': 1}, 'a': {'a': 1}, 'general-purpose': {'g': 1, 'e': 3, 'n': 1, 'r': 2, 'a': 1, 'l': 1, '-': 1, 'p': 2, 'u': 1, 'o': 1, 's': 1}, 'interpreted,': {'i': 1, 'n': 1, 't': 2, 'e': 3, 'r': 2, 'p': 1, 'd': 1, ',': 1}, 'interactive,': {'i': 2, 'n': 1, 't': 2, 'e': 2, 'r': 1, 'a': 1, 'c': 1, 'v': 1, ',': 1}, 'object-oriented,': {'o': 2, 'b': 1, 'j': 1, 'e': 3, 'c': 1, 't': 2, '-': 1, 'r': 1, 'i': 1, 'n': 1, 'd': 1, ',': 1}, 'and': {'a': 1, 'n': 1, 'd': 1}, 'high': {'h': 2, 'i': 1, 'g': 1}, 'level\nprogramming': {'l': 2, 'e': 2, 'v': 1, '\n': 1, 'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}, 'language\n\n\n\n': {'l': 1, 'a': 2, 'n': 1, 'g': 2, 'u': 1, 'e': 1, '\n': 4}}

"""
from collections import Counter
x = Counter("geeksforgeeks")
for i in x.elements():
    print ( i, end = " ")

