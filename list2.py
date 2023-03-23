#loop through list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


#loop through index number
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#using while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#List comprehension : List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list
#without comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#with comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#syntax: newlist = [expression for item in iterable if condition == True]

#Condition
newlist = [x for x in fruits if x != "apple"]
print(newlist)

#iterable: iterable can be any iterable object like set, tuple, list etc
newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)

#set the values to uppercase 
newlist = [x.upper() for x in fruits]
print(newlist)

#set all values in list to hello
newlist = ['hello' for x in fruits]
print(newlist)

#expression also can have condition they have way to manipulate outcome 
#here is way to print 'orange' when 'banana' is there
newlist = [x if x != 'banana' else 'orange' for x in fruits]
print(newlist)

#sort() method is used to sort the list alphanumerically or ascending order
list3 = ["om","jay","jagdish"]
list3.sort()
print(list3)

#sort list numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#sort  the items reverse
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#case sensitive sort : sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#for printing lowercase letters first
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#for reversing the string
thislist = ["a", "b", "c", "d"]
thislist.reverse()
print(thislist) 

