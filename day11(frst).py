'''Write a program where the user enters three numbers, and the program finds and displays the largest number among them.'''



num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
if num1>num2 and num1>num3:
    print(num1,"is the largest number")
elif num2>num1 and num2>num3:
    print(num2,"is the largest number")
else:
    print(num3,"is the largest number")


'''output:
Enter the first number:10
Enter the second number:20
Enter the third number:-65
20 is the largest number'''
