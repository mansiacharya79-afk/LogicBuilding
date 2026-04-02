'''Write a Program to Display All Factors of a Number:
Write a program to find and print all factors of a number entered by the user.'''

num = int(input("Enter a number: "))
print("Factors of" , num , "are:", end =" ")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")


'''output:
Enter a number: 12
Factors of 12 are: 1 2 3 4 6 12 '''