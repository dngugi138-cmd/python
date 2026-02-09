print('==================================================')
# create a python program that prints the loop years in btwn 2000 and 2024
for year in range(2000, 2025):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year)

# research on python function. With both parameters and without parameters