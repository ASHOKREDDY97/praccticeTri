# #  Reverse words in sentence
# sentence = 'I am Ashok'
# words = sentence.split()
# words = reversed(list(words))
# print(" ".join(words))


# #  Revers letters of words in given sentence
# s = "hello"
# a =" ".join(word[::-1] for word in s.split())
# print(a)

# # Print the words with number of occurences in sentence
# a='the quick brown fox jumps over the lazy dog , dog makes sound'
# b=a.split()
# count={}
# for i in b:
#     if i in count:
#         count[i]+=1
#     else:
#         count[i]=1
# print(count)


# #  print each letter how many times repeated in a given words
# a = 'ashokreddy'
# a.split()
# count = {}
# for i in a:
#     if i in count:
#         count[i]+= 1
#     else:
#         count[i] = 1
# print(count)


# # separate non-aplabet number
# def NonAlaph(str):
#     print('non-alpha:',end='')
#     for i in str:
#         if (i.isalpha()== False):
#             print(i,end='')
# NonAlaph('ashok123@')


# # # spearate non-alpha-numberic
# def number(num):
#     print('only numbers:',end='')
#     for i in num:
#         if (i.isalnum() ==False):
#             print(i,end='')
# number('123a@')

# # removing duplicate items in a list
# list1 = [1,2,34,4,4,4,3,1]
# x=list(set(list1))
# print(x)


# # Difference b/w print print and return
# def function_that_prints():
#     print ("I printed")
# def function_that_returns():
#     return("I returned")

# f1 = function_that_prints()
# f2 = function_that_returns()
# print("Now let us see what the values of f1 and f2 are")
# print (f1)
# print (f2)

# ###


# #occurence of a number
# def get_count(arr,size,target_values):
#     cnt = 0
#     for i in range(0,size):
#         if arr[i] == target_values:
#             cnt = cnt+1
#     return cnt
# my_list = [1,2,3,2,3,1,2,1,3,3,2,1,1,1,2,3]
# print('1 occurance :',get_count(my_list,len(my_list),1))
# print('2 occurance :',get_count(my_list,len(my_list),2))
# print('3 occurance :',get_count(my_list,len(my_list),3))


# # Reverse words in sentence
# sentance = "hi i am ashok"
# a = sentance.split()
# #print(split)
# a.reverse()  # reverse
# print(' '.join(a)) #concetenate

# #  scenario dictionary - {"a":1,"b":2} , print result as {1:"a",2"b}
# old_dict = {'a': 1, 'b': 2}
# new_dict = dict([(value, key) for key, value in old_dict.items()])
# print(new_dict)


# #1.print reverse of sentence "Good Morning,I am learning python" 
# # o/p : "nohtyP gnin--- "

# s = "Good Morning,I am learning python"
# print(s[::-1])
# print(len(s))

# # 2. Reverse letters of words in given sentence 
# # o/p: "dooG gninroM I ma gninrael .. "

# s = "Good Morning,I am learning python"
# a =" ".join(word[::-1] for word in s.split())
# print(a)

# #3. print each letter how many times repeated
# a="good morning,i am learning python"
# count={}
# for i in a:
#     if i in count:
#         count[i]+=1
#     else:
#         count[i]=1
# print(count)


# # 4.print vowels and consonants in sentence

# string = "good morning,i am learning python"
# print('Vowels: ')
# for char in string:
#    if char in "aeiouAEIOU":
#       print(char, end=', ')

# print('\nConsonants: ')
# for char in string:
#    if char not in "aeiouAEIOU ":
#       print(char, end=', ')


# # 4.Python program to count vowel or consonant of the given string
# str="good morning,i am learning python"
# vowels=0
# consonants=0
# str.lower()
# for i in str:
#     if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' ):
#            vowels=vowels+1
#     else:
#         consonants=consonants+1
# print("The number of vowels:",vowels)
# print("The number of consonant:",consonants)


# user_input = input('enter the file name you want to read:')
# try:
#     with open(user_input, 'r') as f:
#       myfile = open(user_input)
#       info = myfile.read()
#       print(info)
# except OSError:
#     print("Could not read file:", myfile)
# finally:
#   print('exit')



# import os
# # file is taken from user
# user_input = input('enter the file name you want to read:')  
# myfile = open(user_input)
# info = myfile.read()
# # Remove the leading spaces and newline character
# line = info.strip()
# # lowercase to avoid case mismatch
# line = info.lower()
# # check file is exist or not
# if os.path.exists("practice.txt"):
#     print(info)
# else:
#   print("The file does not exist") 
# data=info.split()
# # counting how many words repeated in a file
# count={}
# for i in data:
#     if i in count:
#         count[i]+=1
#     else:
#         count[i]=1
# #print(count)
# myfile.close()
# # Print the contents of dictionary
# for key in list(count.keys()):
#     print(key, ":", count[key])

# # output
# # hello hello world hello world hello world
# # hello : 4
# # world : 3






# # Open the file in read mode
# text = open("practice.txt", "r")
# # Create an empty dictionary
# d = dict()
  
# # Loop through each line of the file
# for line in text:
#     # Remove the leading spaces and newline character
#     line = line.strip()
#     # lowercase to avoid case mismatch
#     line = line.lower()
#     # Split the line into words
#     words = line.split(" ")
#     print(words)
  
#     # Iterate over each word in line
#     for word in words:
#         # Check if the word is already in dictionary
#         if word in d:
#             # Increment count of word by 1
#             d[word] = d[word] + 1
#         else:
#             # Add the word to dictionary with count 1
#             d[word] = 1
  
# # Print the contents of dictionary
# for key in list(d.keys()):
#     print(key, ":", d[key])


