'''Write a program where the user enters a number , and the program calculates the sum of all natural numbers up to '''

n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i
print("The sum of natural numbers up to", n, "is:", sum)


'''output:
Enter a number: 6
The sum of natural numbers up to 6 is: 21      
'''