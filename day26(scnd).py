'''Find the First Non-Repeating Character
Identify the first character that does not repeat in the string.
'''

string = input("Enter a string: ")
for ch in string:
    if string.count(ch) == 1:
        print("First non-repeating character:", ch)
        break

'''Output
Enter a string: hello world
First non-repeating character: e'''