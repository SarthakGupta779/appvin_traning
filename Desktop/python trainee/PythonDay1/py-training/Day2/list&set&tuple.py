list = ["apple","cherry", 46, "cherry"]
print(list)

#len of list
list = ["apple","cherry", "cherry"]
print(len(list))

#list type
list = ["apple","cherry", 46, "cherry"]
print(type(list))

#change list item
th =  [12,23,64,853,244,25,73]
th[2]=432
print(th)

#Add the item
th =  [12,23,64,853,244,25,73]
th.insert(5,2444)  # we also use extend,append
print(th)

# clear 
th =  [12,23,64,853,244,25,73]
th.clear()
print(th)

#reverse the list
th =  [12,23,64,853,244,25,73]
th.sort(reverse=True)
print(th)
#sort
list = ["apple","sfterry", "cherry"]
list.sort()
print(list)

#tuple...................
thu=("sarthak",)
print(type(thu))

#tuple methoda
thu=("sarthak","apple","sfterry", "cherry")
print(thu[2:])

#tuple changeable
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)

# set method
t = {"apple", "banana", "cherry", "apple"}

print(t)

#set type
t = {"apple", "banana", "cherry", "apple"}

print(len(t))

print(type(t))

#set add item
t = {"apple", "banana", "cherry", "apple"}
t.add("doiehoi")

print(t)
# remove or diecard or del or pop
t = {"apple", "banana", "cherry", "apple"}
t.remove("apple")
print(t)
t.clear()
print(t)

#union or update
t = {"apple", "banana", "cherry", "apple"}
s={1, 2, 3}
x=t.union(s)
         
print(x)

#dictionary
dict = {"brand": "Ford","model": "Mustang","year": 1964}
print(dict)

#dict types
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(dict))


print(dict["year"])
#llen of dic
print(len(dict))

#get method
x=dict.get("model")
x1=dict.keys()
print(x)
print(x1)

#item
a1=dict.items()
print(a1)

# string methods
a = "Hello, World!"
print(a)

#length of string
a = "Hello, World"
print(len(a))

#slicing of string

b = "Hello, World"
print(b[2:8])

#strip
print(a.strip()) 