# Objects can also contain methods. Methods in objects are functions that belong to the object      

# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class

# class student:
#     def __init__(self,name,surname):
#      self.name = name 
#      self.surname = surname

#     def fun(self):
#         print("My name is",self.name,"and surname is",self.surname)

# s = student("Om", "Patil")

# s.fun()

class HOD:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    def fun(self):
        print("Name of HOD is",self.name,"and surname is",self.surname)

p = HOD("Shrikant", "Dhamdhere")
p.surname="Dhamdhere Sir" #Surname updated
p.fun()



