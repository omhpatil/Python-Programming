# To understand the meaning of classes we have to understand the built-in __init__() function.  
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created
# Create a class named Student, use the __init__() function to assign values for name and id

class student:
    def __init__(self,name,id):
     self.name = name 
     self.id = id
  
s = student('Om',54)

print(s.name)
print(s.id)

# The __init__() function is called automatically every time the class is being used to create a new object