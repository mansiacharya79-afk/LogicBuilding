'''Check if Two Strings are Rotations of Each Other
Check if one string is a rotation of another.'''


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Yes ")
else:
    print("No")


'''output
Enter first string: hello
Enter second string: lohel
Yes
'''