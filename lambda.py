# Lambda function can take any numbers of argument but can only have one exoression

x = lambda a : a + 10
print(x(5)) 

# lambda function can take any number of arguments
y = lambda a,b : a*b
print(y(5,6))

# addition of three variable using the lambda function
z = lambda a,b,c : a + b + c
print(z(1,2,3))

# Why Lambda : The power of lambda is better shown when you use them as an anonymous function inside another function.

def myfunc(n):
  return lambda a : a * n
a = myfunc(5)
print(a(10))

