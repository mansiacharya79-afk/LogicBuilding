
'''Count Vowels and Consonants
Count the number of vowels and consonants in a string.
'''

s = input("Enter a string: ")
vowels = "aeiou"
v = 0
c = 0
for ch in s:
    if ch.isalpha():
        if ch.lower() in vowels:
            v += 1
        else:
            c += 1
print("Vowels:", v)
print("Consonants:", c)

'''output
Enter a string: Hello World
Vowels: 3
Consonants: 7
'''