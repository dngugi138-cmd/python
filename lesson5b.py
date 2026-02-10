# functions with parameters
# Parameters: They are values that get passed as arguments given to a function inside of the parenthesis.


def greeting(name):
    print(f'{name} How are you? Hope everything is fine.')

greeting('Dan')
greeting('Nev')
greeting('Nelly')

def message(names):
    print(f'Hello {names}. we shall be having a general meeting on date..... Please avail yourself')

message('Joy')
message('Stephen')

print('================================')
# Create a function that accepts parameters to add two numbers
def addition (x,y):
    sum = x + y
    print('the sum of the numbers is: ', sum)

addition(45,65)
addition(75, 92)