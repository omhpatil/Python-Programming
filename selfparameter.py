# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class.

class Person:
  def __init__(xyz, name, age):
    xyz.name = name
    xyz.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc() 

# here we cam modify age
p1.age = 35
print(p1.age)

# deleted object proporties
del p1.age
print(p1.age)

# deleted object
del p1 
print(p1) # Nameerror : p1 id not defined

# pass statement used avoid error it will print blank page




