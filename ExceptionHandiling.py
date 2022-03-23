# try...except blocks
try:
    a=5
    b='0'
    print(a/b)

except:
    print('Some error occurred.')
print("Out of try except blocks.")



# Catch Specific Error Type
try:
    a=5
    b='0'
    print (a+b)
except TypeError:
    print('Unsupported operation')
print ("Out of try except blocks")

 # Multiple except Blockstry:
try:
    a=5
    b=0
    print (a/b)
except TypeError:
    print('Unsupported operation')
except ZeroDivisionError:
    print ('Division by zero not allowed')
print ('Out of try except blocks')