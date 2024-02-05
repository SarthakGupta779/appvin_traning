def type_checker(*arg_types):
  def decorator(func):
    def wrapper(*args):
      if all(isinstance(arg,arg_type) for arg,arg_type in zip(args[1:],arg_types)): #isinstance do type checking --> x, y (is x is type of y)
        return func(*args)
      else:
        raise TypeError("type of arg provided is wrong")
    return wrapper
  return decorator


class Person:

  @type_checker(str,str,int)
  def __init__(self, first, last, age):
    self.first = first
    self.last = last
    self.age = age

  @property
  def fullname(self):
    return f"{self.first} {self.last}"

  @type_checker(str)
  @fullname.setter
  def change_name(self, name):
    self.first, self.last = name.split(" ")
    return self.first, self.last

  @type_checker(str)
  @fullname.setter
  def change_first(self, f):
    self.first =f
    return self.first

  @type_checker(str)
  @fullname.setter
  def change_last(self, l):
    self.last =l
    return self.last

  @fullname.deleter
  def deleting_name(self):
    self.first = self.last = None
    return None, None

  @property
  def is_adult(self):
    return self.age >=18

  @type_checker(int)
  @is_adult.setter
  def change_age(self,age):
    self.age= age
    return self.age

p=Person("xyz","sharma",50)
print(p.fullname)
p.change_name="rty sharma"
print(p.fullname)
print(p.is_adult)
print(p.deleting_name)


##xyz sharma
##rty sharma
##True
##(None, None)



def type_checker(*arg_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if all(isinstance(arg, arg_type) for arg, arg_type in zip(args[1:], arg_types)):
                return func(*args, **kwargs)
            else:
                raise TypeError(f"Invalid argument types provided for {func.__name__}")

        return wrapper

    return decorator


class Person:
    @type_checker(str, str, int)
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @type_checker(str)
    def change_name(self, name):
        self.first, self.last = name.split(" ")
        return self.first, self.last

    @type_checker(str)
    def change_first(self, f):
        self.first = f
        return self.first

    @type_checker(str)
    def change_last(self, l):
        self.last = l
        return self.last

    @type_checker(None)
    @property
    def deleting_name(self):
        self.first = self.last = None
        return None, None

    @property
    def is_adult(self):
        return self.age >= 18

    @type_checker(int)
    def change_age(self, age):
        self.age = age
        return self.age


p = Person("xyz", "sharma", 50)
print(p.fullname)
p.change_name("rty sharma")
print(p.fullname)
print(p.is_adult)
print(p.deleting_name)


#chaining 
def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def my_function():
    print("Inside the function")

my_function()