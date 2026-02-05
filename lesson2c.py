# A dictionary is a data type that stores data interms of key - value pair.
# It is introduced by use of curly braces {}
# The values stored inside of a dictionary can be of any data type
# To access the valus in a dictionary we use the keys

phonebook = {
    'Benson' : '2547431233',
    'Mary' : '2547641233',
    'Stephen' : '2547451133'
}

# showing the entire dictionary
print(phonebook)
print(type(phonebook))

# print out Benson's number
print(phonebook['Benson'])

print('===========================')

player = {
    'name' : 'Messi',
    'age' : 40,
    'teams' : ['PSG', 'Barcelona', 'Argentina']
}
# the second team he played for
print(player['teams'][1])

# research on if ... else statements in python