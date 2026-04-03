'''Print Factorial Series:
Write a program that prints the factorial of numbers from 1 to N, where the user enters N. '''



num=int(input("Enter a number: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
    print( i,"! =",fact)


'''output:
Enter a number: 5
 1 ! = 1
 2 ! = 2
 3 ! = 6
 4 ! = 24
 5 ! = 120
'''