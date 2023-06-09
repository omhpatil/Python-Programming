# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# Try Block :
#           When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
#           Exception can be handled by using the try block

x = "Kya Bolti Public"

try:
    print(x)
except:
    print("An Exception Occured")
