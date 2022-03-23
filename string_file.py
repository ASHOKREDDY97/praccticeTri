# string

a = 'this is a string in python'
print(type(a))
print(a)
len(a)


# multiple line string
b = '''this is python
       string'''
print(b)
print(len(b))


# string with index number 
greet = 'hello'
print(greet[0])
print(greet[1])
print(greet[2])
print(greet[3])


# string with negative index
greet = 'hello'
print(greet[-1])
print(greet[-2])
print(greet[-3])
print(greet[-4])
print(greet[-5])


# string capiltalize
a = 'hello world'
b = a.capitalize()
print(a)
print(b)


# string casefold
mystr = 'TUTORIALS Teacher'
print(mystr.casefold())
print('HELLO WORLD'.casefold())


# str.center()
greet='Hi'
print(greet.center(4, '-'))
print(greet.center(4, '*'))
print(greet.center(4, '>'))


# string count
greet = 'hello ashok, how are you'
total = greet.count('hello')
print('Number of occerence of "hello":',total)


# string count
a = 'Python is an interpreted,object-oriented,high-level programming language'
a=a.split()
count = {}
for i in a:
    if i in count:
        count[i]+=1
    else:
        count[i]= 1
        print(count)



# separate non-aplabet number
def NonAlaph(str):
    print('non-alpha:',end='')
    for i in str:
        if (i.isalpha()== False):
            print(i,end='')
NonAlaph('ashok123@')
