class Ani:
	def speak(self):
		raise NotImplementedError("not implemented")

class D(Ani):
	def speak(self):
		return "Woof woof dog!"

class C(Ani):
	def speak(self):
		return "Meow cat!"


a = [D(), C()]

for i  in a:
	print(i.speak())
