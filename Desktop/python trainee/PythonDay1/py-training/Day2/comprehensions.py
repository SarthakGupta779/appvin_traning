#list comprehensions
num = [1, 2, 3, 4, 5] 
square = [x ** 2 for x in num] 
print(square)


list = [i for i in range(17) if i % 2 == 0] 
print(list)

#dictionary comprehensioms
input = [1,2,3,4,5,6,7]
   
dict = {v:v ** 3 for v in input if v % 2 == 0}
   
print(dict)

#set comprehensions


input = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
   
set = {v for v in input if v % 2 == 0}
   
print(set)