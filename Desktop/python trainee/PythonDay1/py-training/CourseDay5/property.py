#Property method type 1
class cls:
    def __init__(self,val):
        self.__val=val
    def getv(self):
        print("getting value: ")
        return self.__val
    def setv(self,val):
        print("setting a val: "+val)
        self.__val=val
        
    def delv(self):
        print("deleting")
        del self.__val
    val=property(getv,setv,delv)
x=cls("Appvin")
print(x.val)
x.val="AV"
del x.val

#Deocraotr property using
class cls:
    def __init__(self,val):
        self._val=val
    @property
    def val(self):
        return self._val
    @val.setter
    def val(self,val):
        print("setter value is : "+self._val)
        self._val=val
    @val.deleter
    def val(self):
        del self._val
x1=cls("Alphaversion")
print(x1.val)
x.val="coj"
del x.val

import re  
  
pattern = re.compile(r'^[A-Za-z]+[A-Za-z0-9._-]+@[A-Za-z]+\.(com|org|net)$')  
  
def emailv(email):  
    # if re.fullmatch(regex, email):  
    #   print("The given mail is valid")  
    # else:  
    #   print("The given mail is invalid") 
    match = pattern.findall(email)
    return match 
        
        
text="Contact us at john.doe@example.com or support@company.org for assistance."
res=emailv(text)
print(res)


###
import re

pattern = re.compile(r'[A-Za-z]+[A-Za-z0-9._-]+@[A-Za-z]+\.(com|org|net)')

def emailv(text):
    match = pattern.search(text)
    return match.group() if match else None

text = "Contact us at john.doe@example.com or support@company.org for assistance."
res = emailv(text)
print(res)
