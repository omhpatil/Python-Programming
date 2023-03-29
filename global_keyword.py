# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.

a = 10 # a is bydefault global keyword but value of a changed iin fun and set a as global thatwhy value of a became 20

def fun():
    global a
    a = 20
    print(a)

fun()
print(a)

# a became global variable thatswhy value of a cannot be change inside or outside the function
