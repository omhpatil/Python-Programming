#Lists are used to store multiple items in a single variable.
#list can ordered, changable and have duplicate values
#also list item are indexed 

mylist = ["om","jay","jagdish"]
print(mylist)

#ordered: it list item are ordered and cannot change order of item if we add item in it item will add at the end of list
#changable: we can add, remove and change item in list
#duplication: list item can be of same name or same values

#datatype: list item can be of any datatype (string, int, boolean)
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

#also list can have different datatype
list1 = ["string", 123, True]
print(type(list1))

#list() constructor is used to create list
list4 = list(("om","jay","jagdish"))
print(list4)

#change list item
listitem = ["om", "jay", "jagdish", "hari"]
listitem[1:3] = ["jayjay","harehare"]
print(listitem)

#insert or add item into the list
listitem = ["om", "jay"]
listitem.insert(2,"jagdish")
print(listitem)

#append is also used for adding list item at last position
listitem = ["om","jay"]
listitem.append("jagdish")
print(listitem)

#extend is used for merging two list (also insted of list you can add tuple or dic or set also)
list1 = ["om"]
list2 = ["jay"]
list1.extend(list2)
print(list1)

#remove is used to remove list item 
list = ["om","jay","jagdish"]
list.remove("jagdish")
print(list)

#pop() is also used for remove for list item but at the specific index or by giving index number
list.pop(1)
print(list)

#if u use only pop() method it will remove last item in the list
list.pop()
print(list)

#del keyword also used for delete specific index given item
list1 = ["om","jay","jagdish"]
del list1[0]
print(list1)

#by using only del() keyword all list will be deleted
del list1

list2 = ["om","jay","jagdish"]
list2.clear()
print(list2)




