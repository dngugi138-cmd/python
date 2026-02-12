# 1. Create a Program to Find Simple Interest
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

si = (p * r * t) / 100
print("Simple Interest:", si)

print('=====================================')
# 2. Create a Program to Find Body Mass Index
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)
print("BMI:", bmi)

print('=====================================')
# 3. Create a Program to Find Area of a Triangle.
base = float(input("Enter base: "))
height = float(input("Enter height: "))

area = 0.5 * base * height
print("Area of Triangle:", area)

print('=====================================')
# 4. Create a Program to Find Area of a Circle
radius = float(input("Enter radius: "))
pi = 3.142

area = pi * radius * radius
print("Area of Circle:", area)

print('=====================================')
# 5. Given below dictionary
# shopping = {
# 'sugar': 120,
# 'rice': 200,
# 'milk': 60,
# 'bread': 60
# }

# Do the following
# 1. Print this dictionary
# 2. Find the sum of all items in above dictionary.

#Answer

shopping = {
    "sugar": 120,
    "rice": 200,
    "milk": 60,
    "bread": 60
}

# 1. Print dictionary
print(shopping)

# 2. Sum of all items
total = sum(shopping.values())
print("Total cost:", total)

print('=====================================')
# 6. Please attempt the following question:
# Suppose we have a dictionary:

# person = {'john': 40, 'peter': 45}

# What happens when we try to retrieve a value using the expression print(person['susan']).
# Please show your working on how you arrived to your choice below, give one choice below
# a) Since “susan” is not a value in the set, Python raises a KeyError exception
# b) It is executed fine and no exception is raised, and it returns None
# c) Since “susan” is not a key in the set, Python raises a KeyError exception
# d) Since “susan” is not a key in the set, Python raises a syntax error

#Answer
person = {"john": 40, "peter": 45}
print(person["susan"])

print('=====================================')
# 7. Create a List of town and reverse it.
towns = ["Nairobi", "Mombasa", "Kisumu", "Nakuru"]
towns.reverse()

print(towns)

print('=====================================')
# 8. Create a Loop to Print from 10 to 40
for i in range(10, 41):
    print(i)

print('=====================================')
# 9. Create a Loop to Print from -10 to -50
def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

is_leap(2024)

print('=====================================')
# 10. Create a Function to Check if Year is Leap or Not
def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

is_leap(2024)

print('=====================================')
# 11. Create a Function to Find Body Mass Index.
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

print("BMI:", calculate_bmi(70, 1.75))

print('=====================================')
# 12. Using if statements, write a Python program to check how much a traveler would pay based of distance.
distance = int(input("Enter distance: "))

if distance <= 100:
    cost = 5.00
elif distance <= 500:
    cost = 8.00
elif distance < 1000:
    cost = 10.00
else:
    cost = 12.00

print("Travel cost:", cost)

print('=====================================')
# 13. Create a Python Program to find if number is Odd or Even
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
