# Array :  Python does not have built-in support for Arrays, but Python Lists can be used instead.
# Arrays are used to store multiple values in one single variable.

cars = ["BMW","ODI","BENZ"]
for x in cars:
    print(x)

cars.append("CRETA")
print(cars)

cars.remove("CRETA")
print(cars)

cars1 = ["TOYOTA","RANGE ROVER","JEEPSY"]
cars.extend(cars1)
print(cars)

cars.pop()
print(cars)

cars.pop(1)
print(cars)
