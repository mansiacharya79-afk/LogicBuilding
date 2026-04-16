'''Check Palindrome
Determine if a string reads the same backward as forward.
'''
text=input("Enter a string: ")
if text==text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


'''Output
Enter a string: amma
The string is a palindrome.'''