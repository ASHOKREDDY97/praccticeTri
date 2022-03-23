# Difference b/w print print and return

def function_that_prints():
    print ("I printed")
def function_that_returns():
    return("I returned")
f1 = function_that_prints()
f2 = function_that_returns()
print("Now let us see what the values of f1 and f2 are")
print (f1)
print (f2)

####
def print_a_number(num):
    print(num)

def return_a_number(num):
    return num

def add_three(num):
    return num + 3

f1 = print_a_number(7)
f2 = return_a_number(2)
print (f1)
print (f2)
f3 = add_three(f2)
print (f3)
f4 = add_three(f1)
print (f4)



# Functions
# without parameters, without return type

def welcome_msg():
    print('welcome')
welcome_msg()



# without parameter with return values
#sum of 10 numbers 

def sum_of_first_10_numbers():
    sum = 0
    for i in range(1,10):
        sum = sum+i
    return sum
answer=sum_of_first_10_numbers()
print(answer)



# with parameter,without return type

def welcome_user(name,gender):
    if gender == 'M':
        print('welcome Mr.',name)
    else:
        print('welcome Ms.',name)
name = input('Enter your Name:')
gender = input('Enter your gender(M/F):')
welcome_user(name,gender)



# with parameters,with return type

def calculate_sum(a,b):
  sum = a+b
  return sum
print(calculate_sum(2,3)) 



# list of tuple

LT_data = [(1,2,3),('a','s','h','o','k')]
print('List of Tuple:\n',LT_data)



# Python list of tuples using zip() function

list1 = [1,2,3,4,5],
list2 = ['a','k','r'],
list3  = ['ashok','kumar','reddy']
list_tuple = list(zip(list1,list2,list3))
print('List of Tuple:\n',list_tuple)



# Access the tuple
 
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])



# update the tuple

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)



#for loop with string

for char in 'Hello':
    print (char)




# Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)
myfunc()


# Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)