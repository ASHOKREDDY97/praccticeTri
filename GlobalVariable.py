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


###
def fun1():
  print("welcome")
  fun2()
  return None

def fun2():
  print("hello")
  return None
fun1()
fun2()


# calling from main function
def fun1():
  x=60
  print("welcome")
  print("x value from fun1:",x)
  fun2()
  return None

def fun2():
  print("hello")
  x =10
  print("x value from fun2:",x)
  return None

def main():
  fun1()
  return None

main()

