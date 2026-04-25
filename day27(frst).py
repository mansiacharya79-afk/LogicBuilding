'''Check Anagrams
Determine if two strings are anagrams of each other.
'''

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if sorted(s1) == sorted(s2):
    print(" the strings are Anagrams")
else:
    print(" the strings are Not Anagrams")

'''output
Enter first string: listen
Enter second string: silent
 the strings are Anagrams
'''