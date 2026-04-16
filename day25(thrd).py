'''Count Words in a String
Count the number of words in a sentence.
'''
sentence = input("Enter a sentence: ")
words = sentence.split()   
count = len(words)
print("Number of words:", count)


'''Output
Enter a sentence: Logic building
Number of words: 2'''