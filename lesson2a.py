# Python lists
# A list in python is a colllection of items that are ordered in particular way
# A list is introduced by the use of the square brackets []
# The item of a list are stored inside of indexes. Note: In programming we start counting from index zero (0)
# A list is mutable i.e the contents of a list can be changed.

cars = ['BMW', 'Benz', 'Hiace', 'Prado', 'Probox', 'Mclaren', 'Lamborghini']
print(cars)
print(type(cars))

# Accessing items of a list
print(cars[2])
print('The car on index four is: ', cars[4])

# List slicing - this is creating a list from a given bigger list
print(cars[4:])
print(cars[:4])

# printing from hiace to probox
print(cars[2:5])

# List mutability
# We use the function append to add an item at the end of the list
cars.append('Mercedes')
print(cars)

cars.append('Subaru')
print(cars)

# we use the pop function to remove an item at the end of the list
cars.pop()
print(cars)

#we can use an appendix to add items to a list
cars[5] = 'Pajero'
print(cars)

# we can use a sort function to sort our items in alphabetical order
cars.sort()
print(cars)