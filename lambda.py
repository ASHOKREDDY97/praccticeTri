square = lambda x : x * x
print(square(4))


greet = lambda name: print('Hello ', name) 
greet('Steve')


x = lambda a, b : a * b
print(x(5, 6))


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
