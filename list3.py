#by direct list2 = list2 because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2
list1 = ["om","jay"]
list2 = list1
print(list2)
#here we make change in list1 and list2 also cahnged
list1.append("jagdish")
print(list2)

#list2 will be made like reference only thatswhy use copy() method for copying content
list2 = list1.copy()
print(list2)
#here also we made change but items of list2 will not be updated
list1.remove("jay")
print(list1)
print(list2)

#another way to copy list is
list2 = list(list1)
print(list2)

#1]
#for joining two list
list1 = ["hey kaise"]
list2 = ["ho bhai"]
list3 = list1 + list2
print(list3)

#2]
#second method to join the list
for x in list2:
  list1.append(x)
print(list1)

#3]
#third method to join the list
list1 = ["hey kaise"]
list2 = ["ho bhai"]
list1.extend(list2)
print(list1)


