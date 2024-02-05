arr=[1,3,5,6,7,8,9]
print(arr)

#indexing 
print(arr[2])
print(arr[1:])
arr.sort()
print(arr)
print(arr[-3])

#appending
arr.insert(1,64)
print(arr)
arr.append(832)
print(arr)
#delete
arr.remove(6)
print(arr)

arr.pop()
print(arr)
# arr.clear()
# print(arr)

arr=arr*2
print(arr)

#multidimensional array
ar=[[1,3],[6,8,3],[7,4,74],[90,57,36]]
print(ar[3])
print(ar[3][2])
print(ar[1][-3])

#assert statement

assert 5>2

#in keyword
a=[1,4,5,26,6]
print(4 in a)
print(21 not in a)

#lambda keyword
a1=lambda x:x*3
for i in range(1,4):
    print(a1(i))
    
#tuple concept
tup=(1,24,5,53)
print(tup)
#length
print(len(tup))

#max
print(max(tup))
print(sorted(tup))
print(type(tup))

#set concept
set={1,3,5,44,36}
print(len(set))
print(sorted(set))
print(min(set))
set.add(24)
set.update([12,53,64])
set.discard(12)
print(set)
set.remove(24)
print(set)

set.clear()
print(set)

#module import and working
import math as m
print(m.pi)
from math import *
print(pi)

#directory in os

import os
print(os.getcwd())
print(os.listdir())

# dictionary
d1={1:1,2:4,3:9,4:16,5:25}
print(len(d1))
print(type(d1))
print(d1[3])

d2={x:x*x for x in range(6)}
print(d2)
print(2 in d2)

#fraction
from fractions import Fraction as f
print(f(1.2))

import math
print(math.factorial(7))
print(abs(-67.98))
a=9
print(id(a))

#iterator methods
list=[12,13,14,15,17]
o=iter(list)
print(next(o))
print(next(o))

#functional arguments
def findmax(a,b=72):
    if a>b:
        return a
    else:
        return b
print(findmax(12))

#break statement
for i in range(19):
    if(i>4):
        print(i)
        break
#continue statement
for i in range(1,10):
    if(i%2!=0):
        continue
    print(i)