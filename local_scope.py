# variable created inside the function is called as local scope variablel and can used only inside the function
# vaiable created inside the function in available inside that function

def fun():
    a = 10
    print(a)
fun()

# also local variable can be accessed thorugh the inner function

def fun1(): # here we created first function i.e fun1()
    a = 100

    def fun2(): # here we created first function i.e fun2()
        print(a) # we access variable inside the fun1()
    fun2()
fun1()