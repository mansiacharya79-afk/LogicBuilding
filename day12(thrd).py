'''Write a Program to Find the GCD or HCF of Two Numbers:
Write a program where the user enters two numbers, and the program calculates their greatest common divisor (GCD) or highest common factor (HCF).'''


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    temp = b
    b = a % b
    a = temp

print("The GCD is:", a)



'''output:
Enter first number: 60
Enter second number: 48
The GCD is: 12'''