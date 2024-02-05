# error topic

x = 5
y = "hello"
try:
    z = x + y
except TypeError:
    print(" both are differnt type")
    
    
#finally keyword

try:
	k = 8//0
	print(k)

except ZeroDivisionError:
	print("Can't divide by zero")

finally:
	print('it is executed')

# exception

try: 
	a = 10/0
	print (a) 
except ArithmeticError: 
		print ("it is arithmetic except") 
else: 
	print ("yes.") 
