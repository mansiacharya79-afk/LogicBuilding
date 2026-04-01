'''Write a Program to Calculate the Power of a Number:
Write a program that takes a base and an exponent as input and calculates the power of the base raised to the exponent using both manual calculation and the pow() function.'''

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
result = 1
for i in range(exp):
    result = result * base
print("Result using manual calculation:", result)
print("Result using pow() function:", pow(base, exp))
'''output:
Enter base: 2
Enter exponent: 3
Result using manual calculation: 8
Result using pow() function: 8'''