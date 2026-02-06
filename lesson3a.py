# Boolean - this is a data type that evaluates to true or false

isRaining = False
print(isRaining)
print(type(isRaining))

paidloan = True
print(paidloan)
print(type(paidloan))

# comparison operators: They are used to compare two or more statements and they usually a boolean answer

number1 = 3
number2 = 5

print('is number1 greater than number2? ', number1 > number2)
print('is number1 less than number2? ', number1 < number2)
print('is number1 greater than or equal to number2? ', number1 >= number2)
print('is number1 less than or equal to number2? ', number1 <= number2)
print('is number1 equal to number2? ', number1 == number2)
print('is number1 not equal to number2? ', number1 != number2)

# logical operators
# logical and
# It returns true if and only if the condition/statements evaluates to true
print((3 > 1) and (7 > 1))

# logical or
# it evaluates to true if one of the statements/conditions is true
print((3 > 1) or (7 < 6))

# logical not
# It is used to negate a statement/condition
print(not(90 > 70))