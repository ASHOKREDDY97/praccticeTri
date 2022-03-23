# namedtuple

from collections import namedtuple
a = namedtuple('courses' , 'name , tech')
s = a('data science' , 'python')
print(s)

# deque
from collections import deque
a = ['d' , 'u' , 'r' , 'e' , 'k']
a1 = deque(a)
print(a1)
a1.append('a')
print(a1)
a1.appendleft('e')
print(a1)
a1.pop()
print(a1)
a1.popleft()
print(a1)

# ChainMap

from collections import ChainMap
a = { 1: 'edureka' , 2: 'python'}
b = {3: 'data science' , 4: 'Machine learning'}
c = ChainMap(a,b)
print(c)
a1 = { 5: 'AI' , 6: 'neural networks'}
c1 = c.new_child(a1)
print(c1)

# Counter
from collections import Counter
a = [1,1,1,1,2,3,3,4,3,3,4]
c = Counter(a)
print(c)