'''Print Fibonacci Series:
Write a program to print the Fibonacci series up to a number N entered by the user. '''



num=int(input("Enter the number of terms: "))
f1=0
f2=1
for i in range(num):
    print(f1,end=" ")
    f3=f1+f2
    f1=f2
    f2=f3


'''output:
Enter the number of terms: 10
0 1 1 2 3 5 8 13 21 34'''