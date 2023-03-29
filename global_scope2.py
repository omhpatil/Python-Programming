# If you operate with the same variable name inside and outside of a function, 
# Python will treat them as two separate variables, one available in the 
# global scope (outside the function) and one available in the local scope (inside the function):

a = 10

def fun1():
    a = 20
    print("Value of a in fun1 is :",a)

fun1()

print("Value of a outside the function is :",a)

