'''
Print a Number in Reverse Order:
Write a program where the user enters a number, and the program prints it in reverse order.
'''


num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10          
    reverse = reverse * 10 + digit
    num = num // 10          
print("Reversed number =", reverse)


'''output:
Enter a number: 12345
Reversed number = 54321
'''