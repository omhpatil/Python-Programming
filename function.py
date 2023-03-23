# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function

# creating a function
# In python function is created using the def keyword
def fun():
 print("Creating Function")

#calling function
fun()

# Arguments : information passed using is called as argument
def func(fnmae):
    print(fnmae + "Patil")

func("Om ")
func("Aish ")
func("Shweta ")

# Parameters and Argumments
# The terms parameter and argument can be used for the same thing: information that are passed into a function.
# - A parameter is the variable listed inside the parentheses in the function definition.
# - An argument is the value that is sent to the function when it is called.

def funct(fname,lname):
 print(fname + " " + lname)

funct("Om","Patil")
funct("Aish","Patil")

# *ars (Arbitary Arguments) : If you do not know how many arguments that will be passed into your function, 
#                             add a * before the parameter name in the function definition.
#                             This way the function will receive a tuple of arguments, and can access the items accordingly

def my_function(*lname):
  print("The legend boy is " + lname[2])
my_function("Pat", "Pati", "Patil")

# keyword arguments
# You can also send arguments with the key = value syntax. This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Defaulti  parameter value : If we call the function without argument, it uses the default value:
def my_function(country = "India"):
  print("I am from " + country)
my_function()
my_function("Sweden")
my_function("America")
my_function("Brazil")

# Passing list as a argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)


#function return a value
def function(x):
    return 5 * x
print(function(3))

# Pass statement : function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def func1():
    pass

