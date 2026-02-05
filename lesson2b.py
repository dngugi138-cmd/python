# Tuple
# A tuple is an immutable type of list (It cannot change)
# To introduce a tuple,we can use the parenthesis()

counties = ('Nairobi', 'Mombasa', 'Nakuru', 'Eldoret', 'Kajiado', 'Kisii')
print(counties)
print(type(counties))

# slicing of tuples
print(counties[3:])

# accessing items of a tuple by use od the indexes
print(counties[5])

# Note: Below will generate an error
# Attribute error
# counties.append('Machakos')
# print(counties)