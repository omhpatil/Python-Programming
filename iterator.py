# An iterator is an object that contains a countable number of values

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# string accessing 
mytuple = "jay"
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))