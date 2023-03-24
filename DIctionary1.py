#Loops in dictionary

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

#for printing keys in dictionary
for x in thisdict.keys():
  print(x)

#for printing values in dictionar
for x in thisdict.values():
 print(x)

# copy() method
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dictt = thisdict.copy()
print(dictt)

dictt = dict(thisdict) # also we can make copy of dic using dict() method
print(dictt)

#nested dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
