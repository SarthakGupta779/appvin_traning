#simple function 
def fu():
    print("starting a day with a fun")
fu()

#function with parameter

def add(a,b):
    return a+b
# a=int(input("Enter a first number: "))
# b=int(input("Enter a second number: "))
a,b=23,54
c=add(a,b)
print(f"the addition of {a} and {b} is : ",c)