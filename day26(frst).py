'''Longest Word in a Sentence
Find the longest word in a given sentence.
'''
string=input("Enter the string:")
words=string.split()
length=words[0]
for word in words:
    if(len(word)>len(length)):
        length=word
print("The longest word is:",length)

'''Output
Enter the string: Python programming is fun
The longest word is: programming'''