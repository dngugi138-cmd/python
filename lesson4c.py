# A for loop can also be used to iterate through a list, tuple, string or even a dictionary...

name = 'Dan'

for letter in name:
    if letter == 'a':
        print('This is letter a')
    else:
        print(letter)

print('-------------------')
# Below is a list of counties
counties = ['Nairobi', 'Mombasa', 'Kisumu', 'Eldoret', 'Kajiado', 'Machakos', 'Meru', 'Embu']
print(counties)

for county in counties:
    print(county)

print('-------------------')

if 'Embu' in counties:
    print('County found')
else:
    print('County not found')

print('-------------------')
# The loop can also be used to iterate through a dictionary

player = {
    'name': 'Mbappe',
    'age': 25,
    'teams': ['PSG', 'Monaco', 'France'],
    'nationality': 'French'
}

for key in player:
    print(key)

print('-------------------')

for values in player:
    print(player[values])

print('-------------------')
# loop through the teams the player has played for
for teams in player['teams']:
    print(teams)