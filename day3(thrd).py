'''Write a Program to Find the Quotient and Remainder of Two Integers:
Write a program where the user enters two integers (divisor and dividend) and calculates their quotient and remainder'''





dividend=int(input("Enter the dividend:"))
divisor=int(input("Enter the divisor:"))
quotient=dividend//divisor
print("The quotient is:", quotient)
reminder=dividend%divisor
print("The reminder is:", reminder)


'''Output:
Enter the dividend: 10
Enter the divisor: 3
The quotient is: 3
The reminder is: 1'''