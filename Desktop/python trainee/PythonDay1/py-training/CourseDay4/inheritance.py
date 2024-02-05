# Python program to demonstrate
# single inheritance


class Parent:
	def func1(self):
		print("This function parent")

class Child(Parent):
	def func2(self):
		print("This function child ")


# Driver's code
object = Child()
object.func1()
object.func2()



#multiple inheritance


class M:
	mothername = ""

	def m(self):
		print(self.mothername)

class F:
	fathername = ""

	def f(self):
		print(self.fathername)

class Son(M, F):
	def parents(self):
		print("Father :", self.fname)
		print("Mother :", self.mname)


s1 = Son()
s1.fname = "RAM"
s1.mname = "SITA"
s1.parents()
