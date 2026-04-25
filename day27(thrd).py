'''Remove All Non-Alphabetic Characters
Remove all characters that are not letters.
'''


s = input("Enter a string: ")
result = ""
for ch in s:
    if ch.isalpha():
        result += ch
print("Output:", result)

'''output
Enter a string: Hello i am mansi!!@
Output: Helloiammansi'''