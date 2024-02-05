# parent class
class Person(object):

	# __init is  constructor
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)
#inheritance  

# child class
class Employee(Person):
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post
		Person.__init__(self, name, idnumber)

a = Employee('Rahul', 886012, 200000, "Intern")

a.display()


#data encapsulation
class pc:
    def __init__(self):
        self.maxcp=20000
    def mysell(self):
        print("selling price: {}".format(self.maxcp))
    def setmaxcp(self,price):
        self.maxcp=price
pc1=pc()
pc1.mysell()
pc1.maxcp=30000
pc1.mysell()
#using setter function
pc1.setmaxcp(500000)
pc1.mysell()

#operator overloading
class AddableNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return AddableNumber(self.value + other.value)

    def __str__(self):
        return f"AddableNumber with value {self.value}"

# Creating instances of the AddableNumber class
number1 = AddableNumber(5)
number2 = AddableNumber(3)
# Using the '+' operator with instances of the AddableNumber class
result_number = number1 + number2
print(result_number) 

