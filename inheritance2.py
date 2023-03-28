class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname,year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Om", "Patil",2024)
print(x.graduationyear)
x.printname()



# Here we used the super() fun that inherits the all method and proporties of parent class
# Also when we use super() fun we dont need to use name of the parent class it automatically inherts all method and proporties 

