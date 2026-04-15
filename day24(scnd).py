'''Remove Duplicates from an Array
Remove all duplicates from the given array and return the unique elements..
'''

arr=list(map(int,input("Enter the elements:").split()))
arr=list(set(arr))
print("The unique elements in the array are:",arr)


'''Output:
Enter the elements: 6 7 5 2 9 6 7
The unique elements in the array are: [2, 5, 6, 7, 9]
'''