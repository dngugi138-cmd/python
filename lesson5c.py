# Test 1
# By use of a function that accepts parameters, calculate the simple interest given principal as 45000, rate is 7% and the time taken is 8 years. (si = p*r*t/100)
# Use the same function inside of a loop to calculate two other simple interests. Note use your own principal, rate and time.
# Function that accepts parameters to calculate simple interest
def simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si


# Calculate simple interest using given values
si1 = simple_interest(45000, 7, 8)
print("Simple Interest 1:", si1)


# 2️ Use the same function inside a loop for two other calculations
values = [
    (30000, 5, 4),   # principal, rate, time
    (60000, 6, 3)
]

count = 2
for p, r, t in values:
    si = simple_interest(p, r, t)
    print(f"Simple Interest {count}:", si)
    count += 1
