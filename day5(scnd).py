'''Write a Program to Check Whether a Character is a Vowel or Consonant:
Write a program to check whether a character entered by the user is a vowel (a, e, i, o, u) or a consonant'''


char=input("Enter a character: ")
if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
    print(char,"is a vowel.")
else:
    print(char,"is a consonant.")


'''output:
Enter a character: a
a is a vowel.

output 2:
Enter a character: b
b is a consonant.'''
