set = {"o","m",'i'}
for x in set:
 print(set)

#join two set using union() method
set1 = {1,2,3}
set2 = {4,5,6}
set3 = set1.union(set2)
print(set3)

#update method
set1 = {1,2,3}
set2 = {4,5,6}
set1.update(set2)
print(set1)

#keeps only intersection
m = {"apple","banana", "cherry"}
n = {"google", "microsoft", "apple"}
m.intersection_update(n)
print(m)

#keeps all but not print duplicate values
m = {"apple","banana", "cherry"}
n = {"google", "microsoft", "apple"}
m.symmetric_difference_update(n)
print(m)

#Return a set that contains all items from both sets, except items that are present in both:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)