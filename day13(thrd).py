'''Program to Print Integers in Words:
Write a program that converts each digit of an integer entered by the user into its corresponding word representation.'''


num=input("Enter a number:")
for i in num:
    if i=='0':
        print("Zero",end=" ")
    elif i=='1':
        print("One",end=" ")
    elif i=='2':
        print("Two",end=" ")
    elif i=='3':
        print("Three",end=" ")
    elif i=='4':
        print("Four",end=" ")
    elif i=='5':
        print("Five",end=" ")
    elif i=='6':
        print("Six",end=" ")
    elif i=='7':
        print("Seven",end=" ")
    elif i=='8':
        print("Eight",end=" ")
    elif i=='9':
        print("Nine",end=" ")


'''output:  
Enter a number:657
Six Five Seven '''  
