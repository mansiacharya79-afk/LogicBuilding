'''Write a Python program to create a new dictionary by swapping the keys and values of the given dictionary.'''


dict={"name":"Mansi","age":21,"clg":"NMAMiT"}
new_dict={v:k for k , v in dict.items()}
print("Original Dictionary:", dict)
print("New Dictionary:", new_dict)

'''output
Original Dictionary: {'name': 'Mansi', 'age': 21, 'clg': 'NMAMiT'}
New Dictionary: {'Mansi': 'name', 21: 'age', 'NMAMiT': 'clg'}
'''