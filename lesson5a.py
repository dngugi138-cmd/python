# Python functions 
# They are a block of code/statements that performs a given task/action. They can be reused through out the program to perform diffrent tasks
# Function are defined using the def keyword. (define)
# We have 2 main types of functions i.e :
# 1. In-built functions--> They come with the interpreter i.e print(), pop(), range(), append() etc...
#2. User defined functions--. They are created by aprogrmmer to solve a given task.
# To define a function you need to give it a name followed by parenthesis
# For the functions, it is usually indented and to invoke a function we use the function name.

def greeting():
    print('Hello, how are you?')

greeting()

# below we call the function by use of its name
greeting()

print('================================')
# Additin function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print('The sum of the numbers is: ', sum)

addition()

print('================================')
# create a function that  is able to multiply three values
def multiplication():
    num1 = 10
    num2 = 60
    num3 = 5
    product = num1 * num2 * num3
    print('The product of the numbers is: ', product)

multiplication()

print('================================')
# Below is a division function
def divide():
    number1 = int(input('Enter the first number: '))
    number2 = int(input('Enter the first number: '))
    quotient = number1 / number2
    print('The answer is: ', quotient)
    print("----")

for function in range(3):
    divide()