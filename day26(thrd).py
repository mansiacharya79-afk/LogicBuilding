'''Find All Substrings of a String
Print all possible substrings of a string.
'''


string = input("Enter a string: ")
substrings = []
for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        substrings.append(string[i:j])
print("Substrings:", substrings)


'''Output
Enter a string: abc
Substrings: ['a', 'ab', 'abc', 'b', 'bc', 'c']'''