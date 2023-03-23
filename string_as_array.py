a = 'hello string as array'
print(a[0])
print(a[5]) #at index 5 there is blank space

#looping through a string
for b in "forloop":
 print(b)

c ="string"
print(len(c))


#for checking certain character is present in string or not
text ="this is string practice"
print("string" in text)

#printing if statement if string present in text
text = "this is statement"
if "is" in text:
 print("string mil gaya bhai text mai")
else:
    print("string text mai nahi hai yaar")

#for checking ifnot
text = "this is statement"
if "iss" not in text:
    print("else jaise print krta hu")


#slicing index
t = "this is stetement."
print(t[2:4])

#slice form the start 
print(t[:4])

#slice at the end
print(t[2:])

#negative indexing
print(t[8:-1])

#uppercase
s = "love"
print(s.upper())

#lowercase
s = "Love"
print(s.lower())

#remove white spaces
s = " Hello World "
print(s.strip())

#replacing string
s = "ome"
print(s.replace("e","i"))

#split string
s = "hello world"
print(s.split())

#string concatenation
o = "lo"
s = "ve"
os = o + s
print(os)

#formating string
age = 22
s = "my age is {}"
print(s.format(age))

     

