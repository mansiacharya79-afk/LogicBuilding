'''Write a Program to Find the LCM of Two Numbers:
Write a program where the user enters two numbers, and the program calculates their least common multiple (LCM).'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
for i in range(1, a*b + 1):
    if i % a == 0 and i % b == 0:
        print("LCM is:", i)
        break


'''output:
Enter first number: 12
Enter second number: 15
LCM is: 60'''