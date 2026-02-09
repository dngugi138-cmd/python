# LOOPS -->Sometimes we may need to do a piece of work repeated times in such cses we maty use loops.
#A loop is a control structure that allows us to execute a block of code repeatedly until a certain condition is met.
# There are 2 types of loops in python i.e: The 'for loop' and 'while loop'

# Below is the syntax of a loop in python :
"""
for variable in range(n):
    # block of code to be executed
"""

for greeting in range(5):
    print('Hello Moses', greeting)


print('==================================================')

for number in range(10, 20):
    print(number)

print('==================================================')

# find the even numbers in the range of 50 and 71
for number in range(50, 71, 2):
    print(number)


print('==================================================')

# create a python program that prints the odd numbers from 100 to 150
for number in range(101, 150, 2):
    print(number)

print('==================================================')
# create a program that prints the multiples of 3 starting from 201 to 150
for number in range(201, 149, -3):
    print(number)

print('==================================================')
# create a python program that prints the loop years in btwn 2000 and 2024
for year in range(2000, 2025, 4):
    print(year)