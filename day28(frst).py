'''Find Duplicate Characters in a String
Identify all characters that appear more than once in a string.
'''


s = input("Enter a string: ")
duplicates = []
for ch in s:
    if s.count(ch) > 1 and ch not in duplicates:
        duplicates.append(ch)
print("Duplicate characters:", duplicates)


'''output
Enter a string: programming
Duplicate characters: ['r', 'o', 'g', 'm']
'''