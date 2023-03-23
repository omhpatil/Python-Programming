# Dictionaries are used to store data values in key:value pairs
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

dict = {
  "name": "om",
  "surname": "patil",
  "age": 23
}
print(dict)

#length
print(len(dict))

#The values in dictionary items can be of any data type:
dict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(dict)

#type 
print(type(dict))

#access item
x = dict["year"]
print(x)

#there is also get() method by using you will access item
x = dict.get("colors")
print(x)

# key() method can written all keys present in the dict
x = dict.keys()
print(x)

# adding new key in dict
dict1 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
x = dict1.keys()
y = dict1.values()
print(x)
print(y)
dict1["price"] = 230000 # here added new kay value pair which is bydefault added in the dict
print(x) 
print(y)

# for print item (key:value) pair
x = dict1.items()
print(x)

#for checking specific key is present in the dict
if "year" in dict1:
    print("mila bahi mila")

#change values 
dict1["year"] = 1965
print(dict1)

#update 
dict1.update({"year":2023})
print(dict1)

dict1.pop("year")
print(dict1)

# also you can perform add, remove, pop, del, clear method on the dictionary


