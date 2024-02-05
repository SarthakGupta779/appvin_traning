import re
#search method
if re.search("apex","there will be ape present in string or not tell me ape"):
    print("yes it will present")
else:
    print("it will not present")
    
#findall() and . method
a=re.findall("sun.","if it is sunday i will take a sunbath ")
for i in a:
    print(i)

the="the ape was at the apex level"
for i in re.finditer("ape.",the):
    loc=i.span()
    print(loc)
    print(the[loc[0]:loc[1]])

#square bracket
animal="Cog,rat,mat,fat,dog"
all=re.findall("[Crmfd]og",animal)
for i in all:
    print(i)
print()

#^ not taking the between bracket value
animal="cat,rat,mat,fat,dat"
all1=re.findall("[^crf]at",animal)
for i in all1:
    print(i)
print()

#replace the value
reg=re.compile("[crm]at")
animal=reg.sub("owl",animal)
print(animal)

#backslash problem or issues //
rand="here is there \\stuf"
print(re.search("\\\\stuf",rand))

#space removal
reg=re.compile("\n")
animal=reg.sub(" ",animal)
print(animal)

#number matching \d for 0-9 and \D for not the number
rand="cndilk983"
print(len(re.findall("\d",rand)))
print(re.findall("\D",rand))

#matching whitespace in string
if re.search("\w{4,13}\s\w{1,4}","Sarthak Gupta"):
    print("it is valid full name")
    
# + ooperator in regex
print(len(re.findall("ap+","a as apex bapg")))
print(re.findall("ap +","a as apex new bag"))