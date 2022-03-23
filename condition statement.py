# IF-Elif Condition 

 # Write a program to check whether a person is eligible for voting or not. (accept age from user)
age=int(input("Enter your age"))
if age >=18:
   print("Eligible for voting")
else:
   print("not eligible for voting")

# Write a program to check whether a number entered by user is even or odd.
num = int(input("enter the number:"))
if num % 2 == 0:
    print("even")
else:
    print("odd")

# Write a program to check whether a number is divisible by 7 or not.
num = int(input("enter the number:"))
if num % 7 ==0:
    print("divisible")
else:
    print("not divisible")

'''
Write a program to accept percentage from the user and display the grade according to the following criteria:

         Marks                                    Grade
         > 90                                         A
         > 80 and <= 90                               B
         >= 60 and <= 80                              C
         below 60                                     D
'''
percent = int(input("enter the pecentage:"))
if percent > 90:
    print("Grade is A")
if percent > 80 and percent <= 90:
    print("Grade is B")
if percent >=60 and percent <= 80:
    print("Grade is C")
if percent < 60:
    print("Grade is D")

"""
 Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
    
        Cost price (in Rs)                                       Tax
        > 100000                                                 15 %
        > 50000 and <= 100000                                    10%
        <= 50000                                                 5%
"""

tax = 0 
price = int(input("Enter the price of Bike:"))
if price > 100000:
    tax = 15/100*price
elif price > 50000 and price <= 100000:
    tax = 10/100*price
else:
     tax = 5/100*price
print("Tax to be paid ",tax)

# Write a program to find the largest number out of two numbers excepted from user.
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
if num1 > num2:
     print("greater number is :", num1)
else:
     print("greater number is :", num2)

 # Write a program to check whether a number (accepted from user) is positive or negative.
num = int(input("Enter the Number:"))
if num > 0:
    print("positive")
else:
    print("negative")

# Accept the age of 4 people and display the youngest one?
age1=int(input("Enter age of first person:"))
age2=int(input("Enter age of second person:"))
age3=int(input("Enter age of third person:"))
age4=int(input("Enter age of fourth person:"))
if age1 < age2 and age1 < age3 and age1 < age4:
        print("Age of oldest person is ",age1)
if age2 < age1 and age2 < age3 and age2 < age4:
       print("Age of oldest person is ",age2)
if age3 < age2 and age3 < age1 and age3 < age4:
       print("Age of oldest person is ",age3)
if age4 < age1 and age4 < age2 and age4 < age3:
      print("Age of oldest person is ",age4)

# Write a program to check a character is vowel or not.
char = input("Enter any Alphabets:")
vol = "aeiouAEIOU"
if char in vol:
    print("vowel")
else:
    print("not a vowle")

"""
Accept the number of days from the user and calculate the charge for library according to following :

Till five days : Rs 2/day.

Six to ten days  : Rs 3/day.

11 to 15 days  : Rs 4/day

After 15 days    : Rs 5/day

"""
nd = int(input("Enter no.of days:"))
if nd <= 5:
    amt = nd*2
elif nd >= 6 and nd <= 10:
    amt = nd*3
elif nd >= 11 and nd <= 15:
    amt = nd * 4
else:
    amt = nd * 5
print("Total amount to pay is ", amt)



