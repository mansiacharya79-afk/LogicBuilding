'''Task: Combine the items of two dictionaries into a single new dictionary.
'''

dict1={"name":"Mansi","age":21,"clg":"NMAMiT"}
dict2={"city":"Surathkal","Course":"MCA"}
new_dict= dict1|dict2
print("Merged :",new_dict)

'''output
Merged : {'name': 'Mansi', 'age': 21, 'clg': 'NMAMiT', 'city': 'Surathkal', 'Course': 'MCA'}
'''
