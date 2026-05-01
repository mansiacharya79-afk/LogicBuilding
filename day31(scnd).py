'''Power of a Number
Task: Write a recursive function power(base, exponent) to calculate the value of a base raised to a specific power.
'''

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
print("Result:", power(base, exponent))

'''output
Enter base: 2
Enter exponent: 3
Result: 8'''