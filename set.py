#set: Sets are used to store multiple items in a single variable.
set={"jay","shri","ram"}
print(set)

#set unordered, unchangable and does not allow duplication of values
set = {1,2,3,1}
print(set) #here two 1 items are present in set but set not allow duplication of values thats why printing only one form them

#lenth of set
set = {1,2,3}
x = len(set)
print(x)

#also direct in print function you can use len() method
print(len(set))

# type() operator is used to find datatype of set

# set() constructor is used to create set 

# once set is created you cannot change values into set but you can add values into the set
set = {1,2,3,4}
set.add(5)
print(set) 

set2 = {6,7,8,9}
set.update(set2)
print(set)

#iterable : the object in update() method does not have to be set, it can list, tuple or dictionary
list = [10]
set.update(list)
print(set) 

#because of set is unorderd you dont know which item will be removed
set = {"apple", "banana", "cherry"}
x = set.pop()
print(x)
print(set)
set.clear() #using clear method we can remove all the items in the list
print(set) 
del set2 #deleting set
print(set2)     

