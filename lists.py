# Lists

list =  [1,2,3,"hello",-1,True,1,2,3]
print(list)
print(len(list))

###
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


# Access Items
list  = ['apple','banana','mango','cherry','mango','tomoto']
print(list[0])
print(list[1:5])
print(list[-3:-1])

###
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
thislist.insert(2,"ashok")
print(thislist)
thislist.append("ashok")
print(thislist)

###
list = [1,2,3,4]
list1 = ['ashok','kumar','reddy']
list.extend(list1)
print(list)

###
list = [2,3,4,5,5,6,6]
list.pop(1)
print(list)
list.remove(5)
print(list)

###
list = ['ashok','sai','reddy']
newlist = []
for i in list:
    if "a" in i:
        newlist.append(i)
    print(newlist)

###
empty = []
list = input("Enter Name:")
for i in range(5):
    empty.append(list)
    print(list)


# Write a program to accept 10 numbers from the user, if the number is odd, and then add that number to the list.
odd = []
for i in range(1,11):
    num = int(input("Enter Number:"))
    if(num%2!=0):
        odd.append(num)
        print(odd)
        

# Write a program to find the largest number from the following list.(with using inbuilt function)
a = [23, 12, 45, 67, 55]
a.sort()
print(a)
print(a[-1])

# ###
a = [23, 12, 45, 67, 55]
print('smallest number:',min(a))
print('larest number:',max(a))

# ###
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# ###
a = 'Hi Ashok'
print(a[::-1])

# ###
alist =[1,2,3,4]
print(alist[::-2])

# remove duplicate items from the list
list1 = [1,2,3,4,3,2,1,2]
list2=list(set(list1))
print(list2)
