# function problem

def bill_amount_after_discount(bill_amount,discount_percentage):
    discount_amount = bill_amount*(discount_percentage/100)
    final_amount = bill_amount - discount_amount
    print(discount_amount)
    return final_amount
bill_amount = int(input('Enter the Amount:'))
discount_percentage = int(input('Enter the Discount in percentage:'))
final_amount = bill_amount_after_discount(bill_amount,discount_percentage)
print(final_amount)

# without parameters, without return type
def welcome_msg():
    print('welcome')
welcome_msg()

# without parameter with return values
# sum of 10 numbers 
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

def add(a,b):
    print(f'sum of {a} and {b} is:',add)
    return a+b
print(add(2,4))


####
def f1(*num):
    c = 0
    for i in num:
        c = c+i
        #print(c)
    return c

print(f1(1,2))


# fixed keyword arguments

def fullName(firstName,secondName):
    return f"your name is {firstName} {secondName}"

print(fullName(firstName='ashok',secondName='reddy'))

#Arbitrary Arguments
# **kwargs
def fullName(**kwargs):
    print(kwargs)
    print(type(kwargs))

print(fullName(firstName='ashok',middleName='kumar',lastName='reddy'))# the output is in Dict

# * args
def fullName(*args):
    print(args)
    print(type(args))
print(fullName('ashok','kumar','reddy'))# the output is in tuple

# parameter order prority 
"""
1.parameters
2.* args
3.defalut arguments
4.** kwargs

"""
def displayInfo(a,b,*args,instuctor = 'ashok',**kwargs):
    return [a,b,args,instuctor,kwargs]

#print(displayInfo(1,2,'sai','sree','ashok reddy',firstname='Reddy',lastname='chadive'))
print(displayInfo(1,2,'sai','sree',instuctor='ashok reddy',firstname='Reddy',lastname='chadive'))