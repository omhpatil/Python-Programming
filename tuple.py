#Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable.

tuple1 = ("om","jay","jagdish")
print(tuple1)

#tuples item can be ordered, unchangable and allow duplication of values
#also tuples item are indexed

#allow duplication
tuple1 = ("om","jay","jagdish","om")
print(tuple1)

#tuple length
tuple1 = ("om","jay","jagdish")
print(len(tuple1))

#tuple with one item : To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
tuple1 = ("om",)
print(tuple1)

#datatype in tuple
tuple1 = ("om","jay")
tuple2 = (1,2,3,4,5)
tuple3 = (True,False)

print(type(tuple1))
print(type(tuple2))
print(type(tuple3))

#also tuple can be conatain different datatype items
tuple1 = ("om",1,True)
print(type(tuple1))

#tuple() constuctor is used to make tuple
tuple1 = tuple(("om","jay",1,True))
print(tuple1)

#you can tuple item by using index 
print(tuple1[0:3])

#convert the tuple into list to change it because tuple cannot be changable
x = ("om","jay")
y = list(x)
y[1] = "shriram"
y.insert(1, "jay")
x = tuple(y)
print(x)

#by converting tuple into list you can perform method on list like (remove,del,insert) and then convert it into the tuple

#packing : when we create tuple we values to it called packing
#unpacking : in python also to extract values back into variables is called unpacking
tupple = ("orange","banana","gava")
(white,black,red) = tupple
print(white)
print(black)
print(red)



