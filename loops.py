# #for loop

# # list object
nums = [10, 20, 30, 40, 50]
for i in nums:
    print(i)


# tuple object
nums = (10, 20, 30, 40, 50)
for i in nums:
    print(i)


#for loop with string
for char in 'Hello':
    print (char)


# For Loop with Dictionary
numNames = { 1:'One', 2: 'Two', 3: 'Three'}
for pair in numNames.items():
    print(pair)


#  For Loop with Dictionary
numNames = { 1:'One', 2: 'Two', 3: 'Three'}
for k,v in numNames.items():
    print("key = ", k , ", value =", v)

# For Loop with the range() Function
for i in range(5):
    print(i)

# Exit the For Loop
for i in range(1, 5):
    if i > 2:
        break
    print(i)

# Continue Next Iteration
for i in range(1, 5):
    if i > 3:
        continue
    print(i)

# Write a program to print first 10 even numbers.
for i in range(2,22,2):
     print(i)

 # Write a program to print first 10 odd numbers
for i in range(1,21,2):
    print(i)
    
# Write a program to print table of a number accepted from user.
num = int(input("Enter any number:"))
for i in range(1,11):
    print(num*i)

#Write a program to find the factorial of a number.
num = int(input("Enter any number:"))
f=1
for i in range(1,num+1):
    f=f*i
print("Factorial is",f)

# ##
text = 'python'
for character in text:
    print(character)


# ##
Names = ['ashok','sai','xyz']
for x in Names:
    print(x)


# ##
for count in range(1,6):
    print(count)

# # multiplication
number = int(input('Enter Number:'))
for count in range(1,10):
    product = number * count
    print(number,'*',count,'=',product)


# while loop
count = 0
while count < 5:
    print(count)
    count = count+1

###
count = 5
while count <= 10:
    print(count)
    count = count+1

###
number = int(input('enter an number:'))
count = 1
while count <= 10:
    product=(number*count)
    print(number,'*',count,'=',product)
    count = count+1  