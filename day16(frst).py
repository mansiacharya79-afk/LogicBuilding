'''Write a Program to Check Whether a Number is a Palindrome:
Write a program to determine if a number is a palindrome.
'''

num=input("Enter a number :")
if num==num[::-1]:
    print(num,"is a palindrome number")
else:
    print(num,"is not a palindrome number")


'''output:
Enter a number :454
454 is a palindrome number
'''