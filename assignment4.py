# Qn 1: Function Without Parameters
def area_of_rectangle():
    length = 10
    width = 5
    area = length * width
    print("Area of the rectangle is:", area)

area_of_rectangle()

print('==========================')
# Qn 2: Function With Parameters
def calculate_operations(a, b):
    summation = a + b
    difference = a - b
    product = a * b
    division = a / b
    return summation, difference, product, division

result = calculate_operations(20, 10)
print("Sum:", result[0])
print("Difference:", result[1])
print("Product:", result[2])
print("Division:", result[3])

print('==========================')
# Qn 3: Control Statement (if…elif…else)
def check_number():
    num = int(input("Enter a number: "))

    if num > 0:
        print("The number is Positive")
    elif num < 0:
        print("The number is Negative")
    else:
        print("The number is Zero")

check_number()

print('==========================')
# Qn 4: Loop with Arithmetic
def sum_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print("Sum from 1 to", n, "is:", total)

sum_numbers(10)

print('==========================')
# Qn 5: While Loop
def square_numbers():
    num = int(input("Enter a number: "))
    i = 1

    while i <= num:
        print("Square of", i, "is:", i * i)
        i += 1

square_numbers()
