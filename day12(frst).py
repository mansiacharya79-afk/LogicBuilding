'''Factorial of a Number Using a For Loop:
Write a program to calculate the factorial of a number entered by the user using a for loop.'''



num=int(input("Enter a number: "))
fact=1
for i in range(1, num+1):
    fact*=i
print("The factorial of", num, "is", fact)


'''output: 
Enter a number: 5
The factorial of 5 is 120
'''
