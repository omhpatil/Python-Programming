# #loops in tuple : you can loop through tuple by using for loop
# tuple = ("om","jay","jagdish")
# for x in tuple:
#     print(x)

# #loop through index number
# tuple1 = ("om","jay","jagdish","hari","prabhu")
# for i in range(len(tuple1)):
#  print(tuple1[i])

#while loop
thistuple = ("apple", "banana","cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#join two tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#multiply two tuple
ittuple = ("apple", "banana","cherry")
itstuple = 2 * ittuple
print(itstuple)

#count method in tuple
tuple1 = ("a", "b" , "c", "d", "e", "a")
x = tuple1.count("a")
print(x)

#by using index() method we can search first occurence tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)

