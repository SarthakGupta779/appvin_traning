class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,o):
        return self.a+o.a
A1=A(10)
A2=A(20)
A3=A("ishant")
A4=A(" singh")

print(A1+A2)
print(A3+A4)