'''Write a program to swap two numbers entered by the user.'''


num1=int(input("Enter value of a:"))
num2=int(input("Enter value of b:"))
print("Before Swapping:a=",num1," , b=",num2)
temp=num1
num1=num2
num2=temp
print("After swapping: a=",num1," , b=",num2)

'''output:
Enter value of a:10
Enter value of b:20
Before Swapping:a= 10 , b= 20
After swapping: a= 20 , b= 10'''