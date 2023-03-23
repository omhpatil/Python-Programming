# Range() function : The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number
for x in range(6):
  print(x)

for x in range(2,4):
    print(x)

#The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for x in range(2, 30, 3):
  print(x)

# Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
 print(x)
else:
    print("finally finished from here")

for x in range(6):
  if x == 3: 
    break
  print(x)
  
